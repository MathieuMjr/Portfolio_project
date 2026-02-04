from base import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Status(BaseModel):
    """
    Docstring pour Status
    This class describe the status of a reservation.
    Status names are unique.
    """
    __tablename__ = 'status'

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    reservations = relationship('Reservation', back_populates='status')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
