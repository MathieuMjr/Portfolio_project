from app.models.reservation import Reservation
from app.persistence.reservation_repository import ReservationRepository
from app.models.theme import Theme
from app.persistence.theme_repository import ThemeRepository
from datetime import datetime


def test_reservation_creation(app,
                              user,
                              reservation_type,
                              structure,
                              status):
    res_repo = ReservationRepository()
    theme_repo = ThemeRepository()
    theme_data = {
        'name': 'Préhistoire',
        'reservation_type_id': reservation_type.id
    }
    theme = Theme(**theme_data)
    theme_repo.add(theme)

    data = {
        "author_id": user.id,
        "structure_id": structure.id,
        "reservation_type_id": reservation_type.id,
        "reservation_date": "2026-02-10",
        "hour": "10:00",
        "contact_firstname": "Martin",
        "contact_lastname": "Matin",
        "contact_phone": "0678541717",
        "contact_email": "martin.matin@trodrole.com",
        "contact_role": "Prof d'histoire",
        "price": 200,
        "status_id": status.id,
        "themes_id_list": [theme.id]
    }
    theme_id = data.pop('themes_id_list')
    themes = [theme_repo.get_id(element) for element in theme_id]
    # typecast date :
    data['reservation_date'] = datetime.strptime(
        data['reservation_date'], "%Y-%m-%d").date()
    # typecast time :
    data['hour'] = datetime.strptime(data['hour'], "%H:%M").time()
    reservation = Reservation(**data)
    res_repo.add(reservation)
    reservation.themes = themes

    for key in data:
        assert data[key] == getattr(reservation, key)

    assert theme in reservation.themes
    assert reservation in theme.reservations
    assert reservation.author == user
    assert reservation in user.reservations
    assert reservation.structure == structure
    assert reservation in structure.reservations
    assert reservation.status == status
    assert reservation in status.reservations
    assert reservation.reservation_type == reservation_type
    assert reservation in reservation_type.reservations
