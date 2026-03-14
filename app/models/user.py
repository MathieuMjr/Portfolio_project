from .base import BaseClass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db, bcrypt
from sqlalchemy import (String,
                        ForeignKey,
                        Boolean,
                        Table,
                        Column)

user_reservation_type = Table(
    'user_reservation_type',
    db.metadata,
    Column('user_id',
           String(36),
           ForeignKey('users.id'),
           nullable=False,
           primary_key=True),
    Column('reservation_type_id',
           String(36),
           ForeignKey('reservation_types.id'),
           nullable=False,
           primary_key=True)
)


class User(BaseClass):
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
        String(100),
        nullable=False
    )
    lastname: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(60),
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

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "role": self.role,
            "reservation_types": [
                element.to_dict() for element in self.reservation_types],
            "is_active": self.is_active
        }

    def verify_pwd(self, pwd):
        return bcrypt.check_password_hash(self.password, pwd)

    def hash_pwd(self, pwd):
        hashed = bcrypt.generate_password_hash(pwd)
        self.password = hashed.decode('utf-8')
