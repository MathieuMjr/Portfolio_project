from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import date
from datetime import time
from decimal import Decimal
# from typing import Optional


class ReservationPayload(BaseModel):
    author_id: str = Field(min_length=36)
    structure_id: str = Field(min_length=36)
    reservation_type_id: str = Field(min_length=36)
    reservation_date: date
    hour: time
    contact_firstname: str = Field(min_length=1)
    contact_lastname: str = Field(min_length=1)
    contact_phone: str = Field(min_length=10, max_length=10)
    contact_email: EmailStr
    contact_role: str = Field(min_length=1)
    price: Decimal = Field(gt=100)
    status_id: str = Field(min_length=36)
    themes_id_list: list[str] = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')

    # @field_validator('reservation_date')
    # def check_date(cls, value):
    #     if value < date.today():
    #         raise ValueError('Date cannot be in the past')
    #     return value


# class ReservationUpdate(BaseModel):
#     hour: Optional[time]
#     contact_firstname: Optional[str] = None
#     contact_lastname: Optional[str] = None
#     contact_phone: Optional[str] = None
#     contact_email: Optional[EmailStr] = None
#     contact_role: Optional[str] = None
#     price: Optional[Decimal] = None
#     status_id: Optional[str] = None
#     themes_id_list: Optional[list[str]] = None

#     @field_validator('contact_firstname', 'contact_lastname', 'contact_role')
#     def non_empty_strings(cls, value, field):
#         if value is not None and len(value.strip()) == 0:
#             raise ValueError(f"{field.name} cannot be empty")
#         return value

#     @field_validator('contact_phone')
#     def check_phone(cls, value):
#         if value is not None and len(value) != 10:
#             raise ValueError("contact_phone must be exactly 10 digits")
#         return value

#     @field_validator('price')
#     def check_price(cls, value):
#         if value is not None and value <= 0:
#             raise ValueError("price must be greater than 0")
#         return value

#     @field_validator('themes_id_list')
#     def check_themes(cls, value):
#         if value is not None and len(value) == 0:
#             raise ValueError("themes_id_list cannot be empty")
#         return value
