from pydantic import BaseModel, Field
from app.models.audience_type import AudienceType
from app.models.reservation import Reservation


class AudiencePayload(BaseModel):
    count: int = Field(gt=0)
    # validateur de count positif
    audience_type_id: str = Field(min_length=1)
    reservation_id: str = Field(min_length=1)


class AudienceCreation(BaseModel):
    count: int = Field(gt=0)
    audience_type: AudienceType
    reservation: Reservation
