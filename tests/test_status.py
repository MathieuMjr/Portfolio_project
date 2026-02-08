from app.models.status import Status
from app.persistence.status_repository import StatusRepository
import pytest
from sqlalchemy.exc import IntegrityError


def test_status_creation(app, status_data):
    status_repo = StatusRepository()
    status = Status(**status_data)

    status_repo.add(status)
    for key in status_data:
        assert status_data[key] == getattr(status, key)

    status_2 = Status(**status_data)
    with pytest.raises(IntegrityError):
        status_repo.add(status_2)
