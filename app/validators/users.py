from pydantic import BaseModel, EmailStr
from app.models.reservation_type import ReservationType


class UserPayload(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: bool
    reservation_types: list[str]


class UserCreation(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    role: bool
    reservation_types: list[ReservationType]
