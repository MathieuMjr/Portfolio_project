from .base import BaseClass
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import UniqueConstraint


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
    category: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    order_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    is_school: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )
    audiences = relationship('Audience', back_populates='audience_type')

    __table_args__ = (
        UniqueConstraint(
            "category",
            "order_index",
            name="uq_audience_category_order"
        ),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "order_index": self.order_index,
            "is_school": self.is_school
        }
