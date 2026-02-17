from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserPayload(BaseModel):
    firstname: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    email: EmailStr
    password: str = Field(min_length=1)
    role: bool
    reservation_types: list[str] = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')
