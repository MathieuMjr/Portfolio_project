from app.models.audience_type import AudienceType
from app.persistence.audience_type_repository import AudienceTypeRepository


def create_audience_types():
    audienceT_repo = AudienceTypeRepository()
    data = [
        {
            'name': 'PS',
            'category': 'Maternelle',
            'order_index': 1,
            'is_school': True},
        {
            'name': 'MS',
            "category": 'Maternelle',
            'order_index': 2,
            'is_school': True},
        {
            'name': 'GS',
            "category": 'Maternelle',
            'order_index': 3,
            'is_school': True},
        {
            'name': 'CP',
            "category": 'Primaire',
            'order_index': 1,
            'is_school': True},
        {
            'name': 'CE1',
            "category": 'Primaire',
            'order_index': 2,
            'is_school': True},
        {
            'name': 'CE2',
            "category": 'Primaire',
            'order_index': 3,
            'is_school': True},
        {
            'name': 'CM1',
            "category": 'Primaire',
            'order_index': 4,
            'is_school': True},
        {
            'name': 'CM2',
            "category": 'Primaire',
            'order_index': 5,
            'is_school': True},
        {
            'name': '6e',
            "category": 'Collège',
            'order_index': 1,
            'is_school': True},
        {
            'name': '5e',
            "category": 'Collège',
            'order_index': 2,
            'is_school': True},
        {
            'name': '4e',
            "category": 'Collège',
            'order_index': 3,
            'is_school': True},
        {
            'name': '3e',
            "category": 'Collège',
            'order_index': 4,
            'is_school': True},
        {
            'name': 'Seconde',
            "category": 'Lycée',
            'order_index': 1,
            'is_school': True},
        {
            'name': 'Première',
            "category": 'Lycée',
            'order_index': 2,
            'is_school': True},
        {
            'name': 'Terminale',
            "category": 'Lycée',
            'order_index': 3,
            'is_school': True},
        {
            'name': 'Enfants',
            "category": 'Non scolaires',
            'order_index': 1,
            'is_school': True},
        {
            'name': 'Adultes',
            "category": 'Non scolaires',
            'order_index': 2,
            'is_school': True}
    ]
    for element in data:
        check_element = audienceT_repo.get_by_attribute(
            'name', element['name'])
        if len(check_element) == 0:
            audience_type = AudienceType(**element)
            audienceT_repo.add(audience_type)
