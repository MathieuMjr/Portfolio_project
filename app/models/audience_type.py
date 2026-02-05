from .base import BaseClass
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AudienceType(BaseClass):
    """
    Docstring pour AudienceType
    Audience type describes what an audience is :
    - a name of type CP, CE1, CE2...
    - a boolean telling if the public is school or not
    """
    __tablename__ = 'audience_types'

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    is_school: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )
    audiences = relationship('Audience', back_populates='audience_type')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_school": self.is_school
        }
