from .base import BaseClass
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Structure(BaseClass):
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
                                back_populates='structure')
    structure_type = relationship('StructureType',
                                  back_populates='structures')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "structure_type": self.structure_type.to_dict(),
            "zip_code": self.zip_code,
            "address": self.address,
            "town": self.town,
            "email": self.email,
            "phone": self.phone
        }
