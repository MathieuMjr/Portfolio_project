from .base import BaseClass
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Audience(BaseClass):
    """
    Docstring pour Audience
    Audience describes what an Audience is:
    - count : the number of attendees
    - an audience type : children, adults, classes ?
    - related to a reservation
    """
    __tablename__ = 'audiences'

    count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    audience_type_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('audience_types.id'),
        nullable=False
    )
    reservation_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('reservations.id'),
        nullable=False
    )
    audience_type = relationship('AudienceType',
                                 lazy='joined',
                                 back_populates='audiences')
    reservation = relationship('Reservation', back_populates='audiences')

    def to_dict(self):
        return {
            "id": self.id,
            "reservation_id": self.reservation_id,
            "audience_type": self.audience_type.to_dict(),
            # to_dict car le champs is_school est important
            "count": self.count
        }
