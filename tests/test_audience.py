from app.models.audience import Audience
from app.persistence.audience_repository import AudienceRepository


def test_audience_creation(app, reservation, audience_type):
    audience_repo = AudienceRepository()
    audience_data = {
        'count': 25,
        'audience_type_id':  audience_type.id,
        'reservation_id': reservation.id
    }
    audience = Audience(**audience_data)
    audience_repo.add(audience)

    for key in audience_data:
        assert audience_data[key] == getattr(audience, key)

    assert audience.reservation == reservation
    assert audience in reservation.audiences
    assert audience in audience_type.audiences
    assert audience.audience_type == audience_type
