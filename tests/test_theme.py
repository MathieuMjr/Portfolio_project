import pytest
from app.models.theme import Theme
from app.persistence.theme_repository import ThemeRepository


def test_theme_creation(app, reservation_type):
    theme_repo = ThemeRepository()
    data = {
        'name': 'Préhistoire',
        'reservation_type_id': reservation_type.id
    }
    theme = Theme(**data)
    theme_repo.add(theme)

    for key in data:
        assert data[key] == getattr(theme, key)

    assert theme.reservation_type_id == data['reservation_type_id']
    assert theme.reservation_type == reservation_type

    data_2 = {
        'name': 'Electricité',
        'reservation_type_id': reservation_type.id
    }

    theme_2 = Theme(**data_2)
    theme_repo.add(theme_2)

    assert len(reservation_type.themes) == 2
    assert theme in reservation_type.themes
    assert theme_2 in reservation_type.themes
