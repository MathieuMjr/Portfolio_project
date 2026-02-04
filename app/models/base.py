from extensions import db
from sqlalchemy import Boolean, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from datetime import datetime


class BaseClass(db.Model):
    """
    Docstring pour Base:
    Base is the base model and define fields/attributes and methods
    shared by every objects/entities of the system.
    id : a unique id generated with UUID
    creation_date
    is_active: a boolean functioning as a soft delete for resources
    """
    __abstract__ = True
    id: Mapped[str] = mapped_column(
        String,
        default=lambda: str(uuid.uuid4()),
        primary_key=True,
        nullable=False,
        unique=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False)
    update_date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False)
