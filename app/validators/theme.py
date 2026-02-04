from pydantic import BaseModel
from app.models.reservation_type import ReservationType


class ThemePayload(BaseModel):
    name: str
    reservation_type_id: str


class ThemeCreation(BaseModel):
    name: str
    reservation_type: ReservationType
