from base import BaseModel
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(BaseModel):
    """
    Docstring pour User
    user describes what a user is :
    - a firstname
    - a lastname
    - a unique email
    - a hashed password
    - a role
    """
    __tablename__ = 'users'

    firstname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    lastname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    role: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
    # reservation_types_ids_list = relationship()
    # reservation_ids_list =relationship()
