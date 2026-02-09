import pytest
from app.models.user import User
from app.persistence.user_repository import UserRepository
from sqlalchemy.exc import IntegrityError

# app en argument déclenche l'execution de la fixture avant le test


def test_user_create_get(app, user_data, admin_data):
    """
    Docstring pour test_user_create_get
    Test basic and admin users creation and retrieval
    Test adding a user with an already registered email

    :param app: App in test configuration with memory sqlite
    :type app: SQLAlchemy
    :param user: Fixture with user attributes
    :type user: dict[str, Any]
    :param admin: Fixture with user
    :type admin: dict[str, Any]
    """
    user_repo = UserRepository()

    # --- TEST USER CREATION
    new_1 = User(**user_data)
    user_repo.add(new_1)

    user_retrieved = user_repo.get_id(new_1.id)

    for key in user_data:
        assert user_data[key] == getattr(user_retrieved, key)
    assert user_retrieved.role is False

    # TEST ADMIN CREATION
    new_admin = User(**admin_data)
    user_repo.add(new_admin)

    admin_retrieved = user_repo.get_id(new_admin.id)
    assert admin_retrieved.role is True

    # --- TEST ADDING A USER WITH ALREADY EXISTING EMAIL
    new_2 = User(**user_data)

    with pytest.raises(IntegrityError):
        user_repo.add(new_2)


def test_bad_user(app, bad_user_data):
    user_repo = UserRepository()

    new_user = User(**bad_user_data)

    with pytest.raises(IntegrityError):
        user_repo.add(new_user)


def test_user_reservation_type_relationship(app, user_data, reservation_type):
    user_repo = UserRepository()
    user = User(**user_data)
    user_repo.add(user)

    user.reservation_types.append(reservation_type)

    assert reservation_type in user.reservation_types
    assert user in reservation_type.users
