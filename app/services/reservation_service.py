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
from app.services.errors import (ThemeDontMatchResType,
                                 UnauthorizedAction)

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
        """
        Create a reservation and its audiences.

        :param self: Allow access to object repositories instances
        :param payload: Data send from the front
        """
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

        # Res-theme relationship population
        new_res.themes = themes_obj

        # Commit reservation
        self.res_repo.add(new_res)

        # Audience check (pydantic, ids)
        checked_audiences = []
        for audience in audiences:
            audience['reservation_id'] = new_res.id
            valid_audience = AudiencePayload(**audience).model_dump()
            audience_type_id = valid_audience['audience_type_id']
            check_id(
                'Audience type', audience_type_id, self.audienceT_repo)
            checked_audiences.append(valid_audience)

        # Audience creation after check
        for audience in checked_audiences:
            new_audience = Audience(**audience)
            self.audience_repo.add(new_audience)

        return new_res.to_dict()

    def user_reservations(self, user_id, start, end):
        """
        Retrieves reservations made by a user in a specific
        date interval.

        :param self: Allow access to object repositories instances
        :param user_id: Id of a user
        :param start: Start date of the reservation interval (inclusive)
        :param end: End date of the reservation interval (inclusive)
        """
        user = check_id('User', user_id, self.user_repo)

        user_res = self.res_repo.user_res_beetween(user.id, start, end)
        user_res_list = [res.to_dict() for res in user_res]
        return user_res_list

    def get_by_id(self, reservation_id):
        return check_id('Reservation', reservation_id, self.res_repo)

    def update(self, reservation_id, data, identity, role):
        existing_res = check_id('Reservation', reservation_id, self.res_repo)

        if not role and identity != existing_res.author_id:
            raise UnauthorizedAction('Unauthorized action')

        # Extract audiences dict
        data_audiences = data.pop('audiences')

        # Validate payload
        print("before pydantic")
        valid_payload = ReservationPayload(**data).model_dump()
        print("after pydantic")
        # Remove field that cannot be updated
        valid_payload.pop('author_id')
        valid_payload.pop('structure_id')
        valid_payload.pop('reservation_type_id')
        print("after pop author")

        # Variable for ids
        status_id = valid_payload['status_id']

        # Extract theme_ids
        theme_ids = valid_payload.pop('themes_id_list')

        # Check resources exist via id
        check_id('Status', status_id, self.status_repo)

        # Check themes + build list of theme object for MtM relationship
        res_type = existing_res.reservation_type
        if not res_type:
            raise LookupError('debug res_type relationship')
        themes_obj = []
        for element in theme_ids:
            theme = check_id('Theme', element, self.theme_repo)
            if theme.reservation_type != res_type:
                raise ThemeDontMatchResType(
                    f'{theme.name} is not of {res_type.name} reservation type')
            themes_obj.append(theme)

        # Check audiences
        existing_audiences = existing_res.audiences
        if len(existing_audiences) == 0:
            raise LookupError('Debug existing_audience')

        checked_audiences = []
        for audience in data_audiences:
            audience['reservation_id'] = existing_res.id
            valid_audience = AudiencePayload(**audience).model_dump()
            audience_type_id = valid_audience['audience_type_id']
            check_id(
                'Audience type', audience_type_id, self.audienceT_repo)
            checked_audiences.append(valid_audience)

        for audience in existing_audiences:
            self.audience_repo.hard_delete(audience)

        for audience in checked_audiences:
            new_audience = Audience(**audience)
            self.audience_repo.add(new_audience)

        existing_res.themes = themes_obj
        # on doit commit ça ? comment ?

        # Update in db
        self.res_repo.update(existing_res, valid_payload)
