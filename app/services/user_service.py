from app.models.user import User
from app.persistence.user_repository import UserRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.validators.users import UserPayload, SelfUpdate, UpdateUserAsAdmin
from app.services.utils import check_id, check_unique


class UserServices():
    def __init__(self):
        self.user_repo = UserRepository()
        self.res_type_repo = ReservationTypeRepository()

    def create_user(self, payload):
        # Payload values and type verifications
        valid_payload = UserPayload(**payload).model_dump()

        # extract reservation_types id
        res_type_data = valid_payload.pop('reservation_types')

        # Check email uniqueness:
        check_unique(
            'User', 'email', valid_payload['email'], self.user_repo)

        # Checking and building reservation_types object
        # to populate relationship:
        res_types = []
        for element in res_type_data:
            resT_obj = check_id(
                "Reservation_Type", element, self.res_type_repo)
            res_types.append(resT_obj)

        # User creation:
        new_user = User(**valid_payload)
        new_user.hash_pwd(valid_payload['password'])

        # Populate relationship
        new_user.reservation_types = res_types

        # Add to db
        self.user_repo.add(new_user)

        return new_user.to_dict()

    # --- SELF UPDATE -------------------------------------------------

    def self_update(self, token_identity, data):
        user = check_id('User', token_identity, self.user_repo)
        pwd_dict = SelfUpdate(**data).model_dump()

        user.hash_pwd(pwd_dict['password'])

        self.user_repo.save(user)

    #  --- GET IDENTITY -------------------------------------------
    def get_identity(self, identity, claims):
        user = check_id('User', identity, self.user_repo)
        user_dict = {
            "firstname": user.firstname,
            "lastname": user.lastname,
        }
        if not claims['role']:
            return user_dict
        else:
            user_dict['reservation_types'] = [
                element.to_dict() for element in self.res_type_repo.get_all()
            ]
        return user_dict

    # --- GET USER BY ID ------------------------------------------
    def get_by_id(self, user_id):
        user = self.user_repo.get_id(user_id)
        if not user:
            raise LookupError(f'User {user_id} not found')
        return user.to_dict()

    def patch(self, user_id, data):
        valid_data = UpdateUserAsAdmin(**data).model_dump(exclude_unset=True)

        user = self.user_repo.get_id(user_id)
        if not user:
            raise LookupError(f'User {user_id} not found')

        if 'reservation_types' in valid_data:
            res_types = []
            for reservation in valid_data['reservation_types']:
                res_type = check_id(
                    'Reservation', reservation, self.res_type_repo)
                res_types.append(res_type)
            user.reservation_types = res_types
            valid_data.pop('reservation_types')

        if 'password' in valid_data:
            user.hash_pwd(valid_data['password'])
            valid_data.pop('password')

        if len(valid_data) == 0:
            self.user_repo.save(user)
        else:
            self.user_repo.update(user, valid_data)

    def delete(self, user_id):
        user = self.user_repo.get_id(user_id)
        if not user:
            raise LookupError(f'User {user_id} does not exist')
        self.user_repo.delete(user)
