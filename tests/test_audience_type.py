import pytest
from app.models.audience_type import AudienceType
from app.persistence.audience_type_repository import AudienceTypeRepository
from sqlalchemy.exc import IntegrityError


def test_audiencetype_creation(app, audience_type_data):
    audiencetype_repo = AudienceTypeRepository()

    new_audienceT = AudienceType(**audience_type_data)
    audiencetype_repo.add(new_audienceT)

    audienceT_retrieved = audiencetype_repo.get_id(new_audienceT.id)

    for key in audience_type_data:
        assert audience_type_data[key] == getattr(audienceT_retrieved, key)

    audienceT_2 = AudienceType(**audience_type_data)

    # --- TEST name unicity
    with pytest.raises(IntegrityError):
        audiencetype_repo.add(audienceT_2)


def bad_audience_type(app):
    audiencetype_repo = AudienceTypeRepository()

    audienceT = {'name': 'Collège du Parc'}

    new_audienceT = AudienceType(audienceT)

    with pytest.raises(IntegrityError):
        audiencetype_repo.add(new_audienceT)
