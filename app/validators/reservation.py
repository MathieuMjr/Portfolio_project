from pydantic import BaseModel, Field, field_validator
from datetime import date
from datetime import time
from decimal import Decimal
from app.models.audience import Audience
from app.models.status import Status
from app.models.user import User
from app.models.theme import Theme
from app.models.structure import Structure
from app.models.reservation_type import ReservationType


class ReservationPayload(BaseModel):
    author_id: str = Field(min_length=1)
    structure_id: str = Field(min_length=1)
    reservation_type_id: str = Field(min_length=1)
    reservation_date: date
    # ajouter un validateur pour la date
    # : elle ne doit pas être dans le passé
    hour: time
    contact_firstname: str = Field(min_length=1)
    contact_lastname: str = Field(min_length=1)
    contact_phone: str = Field(min_length=10, max_length=10)
    contact_email: str = Field(min_length=1)
    contact_role: str = Field(min_length=1)
    price: Decimal = Field(gt=0)
    # validateur de price positif
    status_id: str = Field(min_length=1)
    themes_id: list[str] = Field(min_length=1)

    @field_validator('reservation_date')
    def check_date(cls, value):
        if value < date.today():
            raise ValueError('Date cannot be in the past')
        return value


class ReservationCreation(BaseModel):
    reservation_date: date
    # ajouter un validateur pour la date
    # : elle ne doit pas être dans le passé
    hour: time
    contact_firstname: str = Field(min_length=1)
    contact_lastname: str = Field(min_length=1)
    contact_phone: str = Field(min_length=1)
    contact_email: str = Field(min_length=1)
    contact_role: str = Field(min_length=1)
    price: Decimal = Field(gt=0)
    # Validateur de price positif
    author: User
    themes: list[Theme]
    audiences: list[Audience]
    status: Status
    structure: Structure
    reservation_type: ReservationType

    @field_validator('reservation_date')
    def check_date(cls, value):
        if value < date.today():
            raise ValueError('Date cannot be in the past')
        return value
