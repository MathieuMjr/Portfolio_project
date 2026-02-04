from pydantic import BaseModel
from app.models.audience_type import AudienceType
from app.models.reservation import Reservation


class AudiencePayload(BaseModel):
    count: int
    # validateur de count positif
    audience_type_id: str
    reservation_id: str


class AudienceCreation(BaseModel):
    count: int
    # validateur de count positif
    audience_type_id: str
    reservation_id: str
    audience_type: AudienceType
    reservation: Reservation
