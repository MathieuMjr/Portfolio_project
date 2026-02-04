from base import BaseClass
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user import user_reservation_type


class ReservationType(BaseClass):
    """
    Docstring pour ReservationType
    This class describe the kind of possible reservations:
    Exhibition visit, exhibition rent, animation...
    """
    __tablename__ = 'reservation_types'

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    reservations = relationship(
        'Reservation',
        back_populates='reservation_type')

    themes = relationship('Theme',
                          back_populates='reservation_type')

    users = relationship('User',
                         secondary=user_reservation_type,
                         back_populates='reservation_types')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
