"""
Docstring pour tests.test_base

This module test:
- the base class instanciation and persistence:
    - date fields
    - is_active true
- basic repo methods :
    - soft delete
    - get_all
    - get_id

Since soft delete is the delete policy,
it is possible to get or update a soft deleted
object.
Service and API will be in charge of controlling access to
soft delete objects and will be tested with Postman.
"""
from app.persistence.user_repository import UserRepository
from app.models.user import User
import datetime
import uuid


def test_baseclass_fields(app, user_data):
    user_repo = UserRepository()

    new_user = User(**user_data)
    user_repo.add(new_user)

    assert isinstance(new_user.id, str)
    typecast = uuid.UUID(new_user.id)
    assert typecast is not None
    assert isinstance(typecast, uuid.UUID)
    assert new_user.is_active is True
    assert isinstance(new_user.creation_date, datetime.datetime)
    assert isinstance(new_user.update_date, datetime.datetime)
    assert new_user.creation_date <= new_user.update_date


def test_soft_delete(app, admin_data):
    user_repo = UserRepository()

    new_admin = User(**admin_data)
    user_repo.add(new_admin)

    user_repo.delete(new_admin)

    assert new_admin.is_active is False


def test_entity_update(app, admin_data):
    user_repo = UserRepository()

    new_admin = User(**admin_data)
    user_repo.add(new_admin)

    new_name = {'firstname': 'Cunégonde'}

    user_repo.update(new_admin, new_name)

    admin_updated = user_repo.get_id(new_admin.id)

    assert admin_updated.firstname == new_name['firstname']


def test_get_all(app, user_data, admin_data):
    user_repo = UserRepository()

    user_1 = User(**user_data)
    user_repo.add(user_1)
    user_2 = User(**admin_data)
    user_repo.add(user_2)

    # GET ALL
    active_users = user_repo.get_all()
    assert len(active_users) == 2

    user_repo.delete(user_2)

    # SOFT DELETE ONE AND GET ALL
    active_users = user_repo.get_all()
    assert len(active_users) == 1
    assert active_users[0].is_active is True

    # GET ALL EVEN SOFT DELETED
    actives_and_inactives = user_repo.get_all(include_inactive=True)
    assert len(actives_and_inactives) == 2

    # GET ONLY SOFT DELETED
    inactives = user_repo.get_all_deleted()
    assert len(inactives) == 1
    assert inactives[0].is_active is False


def test_get_deleted(app, user):
    user_repo = UserRepository()
    user_repo.delete(user)

    assert user.is_active is False

    retrieved_deleted_user = user_repo.get_id(user.id)

    assert retrieved_deleted_user is not None
    assert retrieved_deleted_user.id == user.id


def test_get_update_deleted(app, user):
    user_repo = UserRepository()
    user_repo.delete(user)

    assert user.is_active is False

    data = {
        'email': 'mathieu@pro.com'
    }

    user_repo.update(user, data)

    for key in data:
        assert data[key] == getattr(user, key)


def test_get_by_attribute(app, user, admin_data):
    user_repo = UserRepository()
    admin = User(**admin_data)
    user_repo.add(admin)

    request = user_repo.get_by_attribute('role', False)

    for element in request:
        assert element.role is False
    assert request[0].firstname == 'Mathieu'

    # INVALIDE ATTRIBUTE

    request_2 = user_repo.get_by_attribute('Age', 30)

    assert request_2 == []
