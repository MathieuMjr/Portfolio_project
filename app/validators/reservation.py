from pydantic import BaseModel
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
    author_id: str
    structure_id: str
    reservation_type_id: str
    reservation_date: date
    # ajouter un validateur pour la date
    # : elle ne doit pas être dans le passé
    hour: time
    contact_firstname: str
    contact_lastname: str
    contact_phone: str
    contact_email: str
    contact_role: str
    price: Decimal
    # validateur de price positif
    status_id: str


class ReservationCreation(BaseModel):
    reservation_date: date
    # ajouter un validateur pour la date
    # : elle ne doit pas être dans le passé
    hour: time
    contact_firstname: str
    contact_lastname: str
    contact_phone: str
    contact_email: str
    contact_role: str
    price: Decimal
    # Validateur de price positif
    author: User
    themes: list[Theme]
    audiences: list[Audience]
    status: Status
    structure: Structure
    reservation_type: ReservationType
