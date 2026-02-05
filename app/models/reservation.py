from .base import BaseClass
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from datetime import time
from decimal import Decimal
from app.extensions import db
from sqlalchemy import (String,
                        Numeric,
                        DateTime,
                        Time,
                        ForeignKey,
                        Table,
                        Column)

reservation_theme = Table(
    'reservation_theme',
    db.metadata,
    Column(
        'reservation_id',
        String,
        ForeignKey('reservations.id'),
        primary_key=True,
        nullable=False),
    Column('theme_id',
           String,
           ForeignKey('themes.id'),
           primary_key=True,
           nullable=False)
    )


class Reservation(BaseClass):
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
    - have a list of themes
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
    reservation_date: Mapped[datetime.datetime] = mapped_column(
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
    author = relationship('User',
                          lazy='joined',
                          back_populates='reservations')

    themes = relationship('Theme',
                          secondary=reservation_theme,
                          lazy='subquery',
                          back_populates='reservations')

    audiences = relationship('Audience',
                             lazy='subquery',
                             back_populates='reservation')

    reservation_type = relationship(
        'ReservationType',
        lazy='joined',
        back_populates='reservations')

    status = relationship('Status',
                          lazy='joined',
                          back_populates='reservations')

    structure = relationship('Structure',
                             lazy='joined',
                             back_populates='reservations')

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status.to_dict(),
            "structure": self.structure.to_dict(),
            "reservation_date": self.reservation_date.isoformat(),
            "hour": self.hour.isoformat(),
            "reservation_type": self.reservation_type.to_dict(),
            "themes": [theme.to_dict() for theme in self.themes],
            "price": float(self.price),  # float pour JS
            "contact": {"firstname": self.contact_firstname,
                        "lastname": self.contact_lastname,
                        "email": self.contact_email,
                        "phone": self.contact_phone,
                        "role": self.contact_role
                        },
            "audiences": [
                audience.to_dict() for audience in self.audiences]
        }
