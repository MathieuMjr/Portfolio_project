from app.models.audience_type import AudienceType
from app.persistence.audience_type_repository import AudienceTypeRepository


def create_audience_types():
    audienceT_repo = AudienceTypeRepository()
    data = [
        {'name': 'PS', 'is_school': True},
        {'name': 'MS', 'is_school': True},
        {'name': 'GS', 'is_school': True},
        {'name': 'CP', 'is_school': True},
        {'name': 'CE1', 'is_school': True},
        {'name': 'CE2', 'is_school': True},
        {'name': 'CM1', 'is_school': True},
        {'name': 'CM2', 'is_school': True},
        {'name': '6e', 'is_school': True},
        {'name': '5e', 'is_school': True},
        {'name': '4e', 'is_school': True},
        {'name': '3e', 'is_school': True},
        {'name': 'Seconde', 'is_school': True},
        {'name': 'Première', 'is_school': True},
        {'name': 'Terminale', 'is_school': True},
        {'name': 'Enfants', 'is_school': True},
        {'name': 'Adultes', 'is_school': True}
    ]
    for element in data:
        check_element = audienceT_repo.get_by_attribute(
            'name', element['name'])
        if len(check_element) == 0:
            audience_type = AudienceType(**element)
            audienceT_repo.add(audience_type)
