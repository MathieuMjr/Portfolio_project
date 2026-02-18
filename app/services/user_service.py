from app.models.user import User
from app.persistence.user_repository import UserRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.validators.users import UserPayload
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

    def get_by_id(self, user_id):
        return self.user_repo.get_id(user_id).to_dict()

    def put(self, user_id, data):
        user = self.user_repo.get_id(user_id)
        if 'email' in data:
            check_unique('User', 'email', data['email'], self.user_repo)
        if 'password' in data:
            user.hash_pwd(data['password'])
            data.pop('password')
        if user:
            self.user_repo.update(user, data)

    def delete(self, user_id):
        user = self.user_repo.get_id(user_id)
        if not user:
            raise LookupError(f'User {user_id} does not exist')
        self.user_repo.delete(user)
