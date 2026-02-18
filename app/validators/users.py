from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator
from typing import Optional


class UserPayload(BaseModel):
    firstname: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    email: EmailStr
    password: str = Field(min_length=1)
    role: bool
    reservation_types: list[str] = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    reservation_types: Optional[list[str]] = None

    @field_validator("password")
    def password_min_len(cls, value):
        if value is not None and len(value) < 5:
            raise ValueError("Password too short")
        return value

    @field_validator("reservation_types")
    def reservation_types_min_len(cls, value):
        if value is not None and len(value) < 1:
            raise ValueError("Reservation types cannot be empty")
        return value
