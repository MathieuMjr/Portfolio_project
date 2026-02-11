from app.models.user import User
from app.persistence.user_repository import UserRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.validators.users import UserPayload


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
        check_user = self.user_repo.get_by_attribute(
            'email', valid_payload['email'])
        if len(check_user) != 0:
            raise LookupError('Email already registered')

        # Checking and building reservation_types object
        # to populate relationship:
        res_types = []
        for element in res_type_data:
            resT_obj = self.res_type_repo.get_id(element)
            if resT_obj is None or not resT_obj.is_active:
                raise LookupError(f'Reservation_type: {element} not found')
            else:
                res_types.append(resT_obj)

        # User creation:
        new_user = User(**valid_payload)
        print('user obj created')
        new_user.hash_pwd(valid_payload['password'])
        self.user_repo.add(new_user)

        # Populate relationship
        new_user.reservation_types = res_types

        return new_user.to_dict()
