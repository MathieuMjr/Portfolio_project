from app.models.user import User
from app.persistence.user_repository import UserRepository
from app.persistence.reservation_type_repository import ReservationTypeRepository
from app.validators.users import UserPayload
from pydantic import ValidationError


class UserServices():
    def __init__(self):
        self.user_repo = UserRepository()
        self.res_type_repo = ReservationTypeRepository()
# accès au token identity depuis service ? Vérif à faire côté

    def create_user(self, payload):
        try:
            valid_payload = UserPayload(**payload).model_dump()
            res_type_data = valid_payload.pop('reservation_types')

            # check admin role
            # check existing user (via email)
            new_user = User(**valid_payload)
            res_types = [
                self.res_type_repo.get_id(element)
                for element in res_type_data]

            new_user.reservation_types = res_types

            self.user_repo.add(new_user)

            return new_user.to_dict()
        except ValidationError:
            raise
        # except LookupError:
            # raise LookupError('Email already registered')
