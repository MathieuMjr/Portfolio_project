from base import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Theme(BaseModel):
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
        String,
        nullable=False
    )
    reservation_type_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('reservation_types.id'),
        nullable=False
    )
    # reservation_type_id= relationship()
