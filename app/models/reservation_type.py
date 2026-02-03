from base import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ReservationType(BaseModel):
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
    # themes_ids_list = relationship()
