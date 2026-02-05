from pydantic import BaseModel, Field
from app.models.reservation_type import ReservationType


class ThemePayload(BaseModel):
    name: str = Field(min_length=1)
    reservation_type_id: str = Field(min_length=1)


class ThemeCreation(BaseModel):
    name: str = Field(min_length=1)
    reservation_type: ReservationType
