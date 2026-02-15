# Models
from app.models.reservation import Reservation
from app.models.audience import Audience

# Repos
from app.persistence.reservation_repository import ReservationRepository
from app.persistence.audience_repository import AudienceRepository
from app.persistence.audience_type_repository import AudienceTypeRepository
from app.persistence.user_repository import UserRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.persistence.structure_repository import StructureRepository
from app.persistence.status_repository import StatusRepository
from app.persistence.theme_repository import ThemeRepository

# Pydantics
from app.validators.reservation import ReservationPayload
from app.validators.audience import AudiencePayload

# Errors
from app.services.errors import (ThemeDontMatchResType)

# Check_id utils
from app.services.utils import check_id


class ReservationService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.res_repo = ReservationRepository()
        self.struct_repo = StructureRepository()
        self.resT_repo = ReservationTypeRepository()
        self.status_repo = StatusRepository()
        self.theme_repo = ThemeRepository()
        self.audience_repo = AudienceRepository()
        self.audienceT_repo = AudienceTypeRepository()

    def create_reservation(self, payload):
        # Extract audiences dict
        audiences = payload.pop('audiences')

        # Validate payload
        valid_payload = ReservationPayload(**payload).model_dump()

        # Variable for ids
        status_id = valid_payload['status_id']
        structure_id = valid_payload['structure_id']
        res_type_id = valid_payload['reservation_type_id']
        author_id = valid_payload['author_id']

        # Extract theme_ids
        theme_ids = valid_payload.pop('themes_id_list')

        # Check resources exist via id
        check_id('Status', status_id, self.status_repo)
        check_id('Structure', structure_id, self.struct_repo)
        res_type = check_id('Reservation type', res_type_id, self.resT_repo)
        check_id('User', author_id, self.user_repo)

        # Check themes + build list of theme object for MtM relationship
        themes_obj = []
        for element in theme_ids:
            theme = check_id('Theme', element, self.theme_repo)
            if theme.reservation_type != res_type:
                raise ThemeDontMatchResType(
                    f'{theme.name} is not of {res_type.name} reservation type')
            themes_obj.append(theme)

        # Create new reservation
        new_res = Reservation(**valid_payload)
        self.res_repo.add(new_res)

        # Audience check (pydantic, ids) + creation
        for audience in audiences:
            audience['reservation_id'] = new_res.id
            valid_audience = AudiencePayload(**audience).model_dump()
            audience_type_id = valid_audience['audience_type_id']
            check_id(
                'Audience type', audience_type_id, self.audienceT_repo)
            new_audience = Audience(**valid_audience)
            self.audience_repo.add(new_audience)

        # Res-theme relationship population
        new_res.themes = themes_obj

        return new_res.to_dict()

    def user_reservations(self, user_id, start, end):
        user = check_id('User', user_id, self.user_repo)

        user_res = self.res_repo.user_res_beetween(user.id, start, end)
        user_res_list = [res.to_dict() for res in user_res]
        return user_res_list
