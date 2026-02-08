import sys
from pathlib import Path
import pytest
from app.extensions import db
from app import create_app
from config import TestingConfig

sys.path.append(str(Path(__file__).resolve().parent))


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()


@pytest.fixture
def user():
    return {
        'firstname': 'Mathieu',
        'lastname': 'Mjr',
        'email': 'trulu@yopla.fr',
        'password': '123mdp!',
        'role': False
        }


@pytest.fixture
def bad_user():
    return {
        'firstname': 'Mathieu',
        'lastname': 'Mjr',
        'email': 'trulu@yopla.fr',
        # pwd missing
        'role': False
    }


@pytest.fixture
def admin():
    return {
        'firstname': 'Diana',
        'lastname': 'Boss',
        'email': 'owow@kotools.fr',
        'password': '0000lol',
        'role': True
        }


@pytest.fixture
def structure_type():
    return {
        'name': 'Ecole primaire',
        'is_school': True
    }


@pytest.fixture
def structure(type_id):
    return {
        'name': 'Ecole Saint-Joseph',
        'phone': '0380403324',
        'email': 'ecole@st-jo.fr',
        'zip_code': '21000',
        'address': '2 rue du coquelicot',
        'town': 'Dijon',
        'structure_type': type_id
    }


@pytest.fixture
def reservation_type():
    return {
        'name': 'Animation'
    }


@pytest.fixture
def theme(reservation_type_id):
    return {
        'name': 'Retour vers la Préhistoire',
        'reservation_type_id': reservation_type_id
    }


@pytest.fixture
def status():
    return {
        'name': 'En attente signature'
    }


@pytest.fixture
def audience_type():
    return {
        'name': 'CE2',
        'is_school': True
    }


@pytest.fixture
def reservation(status_id,
                structure_id,
                user_id,
                theme_id,
                reservation_type_id):
    return {
        "author_id": user_id,
        "structure_id": structure_id,
        "reservation_type_id": reservation_type_id,
        "reservation_date": "2026-02-10",
        "hour": '10:00',
        "contact_firstname": "Martin",
        "contact_lastname": "Matin",
        "contact_phone": "0678541717",
        "contact_email": "martin.matin@trodrole.com",
        "contact_role": "Prof d'histoire",
        "price": 200,
        "status_id": status_id,
        "themes_id_list": theme_id
    }


@pytest.fixture
def audience(audience_type_id, reservation_id):
    return {
        'count': 25,
        'audience_type_id': audience_type_id,
        'reservation_id': reservation_id
    }
