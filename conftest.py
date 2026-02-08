"""
This module contains some fixtures for pytest:
- to provide standard data in payload format for entity creation testing
- to provide standard persisted ORM objects
    (once their creation has been successfully tested)

These fixtures goals is to test :
- repositories methods
- entity creation
- entity persistence
- entities unicity
- db integrity (not null values)
"""

import sys
from pathlib import Path
import pytest
from app.extensions import db
from app import create_app
from config import TestingConfig
from app.models.user import User
from app.persistence.user_repository import UserRepository
from app.models.structure_type import StructureType
from app.persistence.structure_type_repository import StructureTypeRepository
from app.models.audience_type import AudienceType
from app.persistence.audience_type_repository import AudienceTypeRepository
from app.models.status import Status
from app.persistence.status_repository import StatusRepository
from app.models.reservation_type import ReservationType
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.models.structure import Structure
from app.persistence.structure_repository import StructureRepository
from app.models.theme import Theme
from app.persistence.theme_repository import ThemeRepository
from app.models.reservation import Reservation
from app.persistence.reservation_repository import ReservationRepository
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parent))


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()

# USER FIXTURES ---------------------------------------


@pytest.fixture
def user_data():
    return {
        'firstname': 'Mathieu',
        'lastname': 'Mjr',
        'email': 'trulu@yopla.fr',
        'password': '123mdp!',
        'role': False
        }


@pytest.fixture
def bad_user_data():
    return {
        'firstname': 'Mathieu',
        'lastname': 'Mjr',
        'email': 'trulu@yopla.fr',
        # pwd missing
        'role': False
    }


@pytest.fixture
def admin_data():
    return {
        'firstname': 'Diana',
        'lastname': 'Boss',
        'email': 'owow@kotools.fr',
        'password': '0000lol',
        'role': True
        }


@pytest.fixture
def user(user_data):
    user_repo = UserRepository()
    user = User(**user_data)
    user_repo.add(user)
    return user


# STRUCTURE TYPE FIXTURE ------------------------------


@pytest.fixture
def structure_type_data():
    return {
        'name': 'Ecole primaire',
        'is_school': True
    }


@pytest.fixture
def structure_type(structure_type_data):
    repo = StructureTypeRepository()
    structureT = StructureType(**structure_type_data)
    repo.add(structureT)
    return structureT


# STRUCTURE FIXTURE -----------------------------------------------


@pytest.fixture
def structure(structure_type):
    repo = StructureRepository()
    data = {
        'name': 'Ecole Saint-Joseph',
        'phone': '0380403324',
        'email': 'ecole@st-jo.fr',
        'zip_code': '21000',
        'address': '2 rue du coquelicot',
        'town': 'Dijon',
        'structure_type_id': structure_type.id
    }
    structure = Structure(**data)
    repo.add(structure)
    return structure


# RESERVATION TYPE FIXTURES -----------------------------------------


@pytest.fixture
def reservation_type_data():
    return {
        'name': 'Animation'
    }


# RESERVATION_TYPE FIXTURES ----------------------------------------


@pytest.fixture
def reservation_type(reservation_type_data):
    rt_repo = ReservationTypeRepository()
    rt = ReservationType(**reservation_type_data)
    rt_repo.add(rt)
    return rt


@pytest.fixture
def theme(reservation_type):
    repo = ThemeRepository()
    data = {
        'name': 'Retour vers la Préhistoire',
        'reservation_type_id': reservation_type.id
    }
    theme = Theme(**data)
    repo.add(theme)
    return theme


# STATUS FIXTURES -------------------------------------------------------------


@pytest.fixture
def status_data():
    return {
        'name': 'En attente signature'
    }


@pytest.fixture
def status(status_data):
    status_repo = StatusRepository()
    status = Status(**status_data)
    status_repo.add(status)
    return status


# AUDIENCE TYPE FIXTURES -------------------------------------------------


@pytest.fixture
def audience_type_data():
    return {
        'name': 'CE2',
        'is_school': True
    }


@pytest.fixture
def audience_type(audience_type_data):
    audiencetype_repo = AudienceTypeRepository()
    new_audienceT = AudienceType(**audience_type_data)
    audiencetype_repo.add(new_audienceT)
    return new_audienceT


# RESERVATION FIXTURE --------------------------------------------------

@pytest.fixture
def reservation(status,
                structure,
                user,
                theme,
                reservation_type):
    data = {
        "author_id": user.id,
        "structure_id": structure.id,
        "reservation_type_id": reservation_type.id,
        "reservation_date": datetime.strptime("2026-02-10", "%Y-%m-%d").date(),
        "hour": datetime.strptime('10:00', "%H:%M").time(),
        "contact_firstname": "Martin",
        "contact_lastname": "Matin",
        "contact_phone": "0678541717",
        "contact_email": "martin.matin@trodrole.com",
        "contact_role": "Prof d'histoire",
        "price": 200,
        "status_id": status.id,
        "themes": [theme]
    }
    res_repo = ReservationRepository()
    reservation = Reservation(**data)
    res_repo.add(reservation)
    return reservation
