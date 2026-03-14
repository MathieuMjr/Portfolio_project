from .base import BaseClass
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .reservation import reservation_theme


class Theme(BaseClass):
    """
    Docstring pour Theme
    Theme describes what a theme is:
    - A name - not unique because maybe animation and exhibition
        could have the same theme.
    - A reservation_type telling if the theme is related to an exhibition,
        animation, or else.
    """
    __tablename__ = 'themes'

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    reservation_type_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey('reservation_types.id'),
        nullable=False
    )
    reservation_type = relationship('ReservationType',
                                    back_populates='themes')

    reservations = relationship('Reservation',
                                secondary=reservation_theme,
                                back_populates='themes')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "reservation_type": self.reservation_type.to_dict()
        }
