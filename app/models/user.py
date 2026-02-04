from base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from sqlalchemy import (String,
                        ForeignKey,
                        Boolean,
                        Table,
                        Column)

user_reservation_type = Table(
    'user_reservation_type',
    db.metadata,
    Column('user_id',
           String,
           ForeignKey('users.id'),
           nullable=False,
           primary_key=True),
    Column('reservation_type_id',
           String,
           ForeignKey('reservation_types.id'),
           nullable=False,
           primary_key=True)
)


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
    reservation_types = relationship('ReservationType',
                                     secondary=user_reservation_type,
                                     lazy='subquery',
                                     back_populates='users')

    reservations = relationship('Reservation',
                                back_populates='author')
