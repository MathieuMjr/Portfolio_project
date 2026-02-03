from base import BaseModel
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class StructureType(BaseModel):
    """
    Docstring pour StructureType
    StructureType describes what a type of structure is.
    - a name (the type) that is unique : Primary school, High school,
        Library, etc.
    - is_school: A boolean tell if the structure is a school or not.
    """
    __tablename__ = 'structure_types'

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    is_school: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
    # structure = relationship()
