from base import BaseModel
from sqlalchemy import String, Numeric, DateTime, Time, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from datetime import time
from decimal import Decimal


class Reservation(BaseModel):
    """
    Docstring pour Reservation
    Reservation describes what a reservation is:
    - authored by a user
    - have a date
    - have an hour
    - have a status
    - made for a structure
    - have contact informations
    - have price
    - is for a reservation type
    - have a list of audiences
    """
    __tablename__ = 'reservations'

    author_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('users.id'),
        nullable=False
    )
    structure_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('structures.id'),
        nullable=False
    )
    reservation_type_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('reservation_types.id'),
        nullable=False
    )
    date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    hour: Mapped[time] = mapped_column(
        Time,
        nullable=False
    )
    contact_firstname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    contact_lastname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    contact_phone: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    contact_email: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    contact_role: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    status_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('status.id'),
        nullable=False
    )
    # author_id =relationship()
    # themes_ids_list=relationship()
    # audience_ids_list=relationship()
    # reservation_type_id = relationship()
