from .base import BaseClass
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Status(BaseClass):
    """
    Docstring pour Status
    This class describe the status of a reservation.
    Status names are unique.
    """
    __tablename__ = 'status'

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )
    reservations = relationship('Reservation', back_populates='status')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
