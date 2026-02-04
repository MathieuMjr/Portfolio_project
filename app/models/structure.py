from base import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Structure(BaseModel):
    """
    Docstring pour Structure
    Structure describes what a structure is:
    - a Name that is unique (structures can't have the same name)
    - a phone number
    - an email
    - a zip code
    - a town
    - a structure type
    - a list of reservation
    """
    __tablename__ = 'structures'

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    phone: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    email: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    zip_code: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    address: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    town: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    structure_type_id: Mapped[str] = mapped_column(
        String,
        ForeignKey('structure_types.id'),
        nullable=False
    )

    reservations = relationship('Reservation',
                                lazy='joined',
                                back_populates='structure')
    structure_type = relationship('StructureType',
                                  lazy='joined',
                                  back_populates='structures')
