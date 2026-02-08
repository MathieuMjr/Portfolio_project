import pytest
from app.models.reservation_type import ReservationType
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from sqlalchemy.exc import IntegrityError


def test_reservation_type_repository(app, reservation_type_data):
    rt_repo = ReservationTypeRepository()
    rt = ReservationType(**reservation_type_data)

    rt_repo.add(rt)

    for key in reservation_type_data:
        assert reservation_type_data[key] == getattr(rt, key)

    rt_2 = ReservationType(**reservation_type_data)

    with pytest.raises(IntegrityError):
        rt_repo.add(rt_2)
