import pytest
from app.models.user import User


def test_user():
    user = User(
        firstname='Mathieu',
        lastname='Mjr',
        email='trulu@yopla.fr',
        password='123mdp!',
        role=False)
    assert user.firstname == 'Mathieu'
    assert user.lastname == 'Mjr'
    assert user.email == 'trulu@yopla.fr'
    assert user.password == '123mdp!'
    assert user.role is False

def test_structure():
    