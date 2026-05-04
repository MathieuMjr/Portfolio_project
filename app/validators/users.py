from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator
from typing import Optional


class UserPayload(BaseModel):
    firstname: str = Field(description="Firstname of a user",
                           min_length=1)
    lastname: str = Field(description="Lastname of a user",
                          min_length=1)
    email: EmailStr = Field(description="Email of a user")
    password: str = Field(description="Password of a user",
                          min_length=5)
    role: bool = Field(description="Is the new user an admin or not")
    reservation_types: list[str] = Field(
        description="List of reservation type IDs the user "
        "is authorized to use",
        min_length=1)

    model_config = ConfigDict(extra='forbid')


class SelfUpdate(BaseModel):
    password: str = Field(min_length=5)

    model_config = ConfigDict(extra='forbid')


class UpdateUserAsAdmin(BaseModel):
    password: Optional[str] = None
    role: Optional[bool] = None
    is_active: Optional[bool] = None
    reservation_types: Optional[list[str]] = None

    model_config = ConfigDict(extra="forbid")

    @field_validator("password")
    def password_min_len(cls, value):
        if value is not None and len(value) < 4:
            raise ValueError("Password too short")
        return value

    @field_validator("reservation_types")
    def reservation_types_min_len(cls, value):
        if value is not None and len(value) < 1:
            raise ValueError("Reservation types cannot be empty")
        return value
