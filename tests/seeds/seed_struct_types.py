from app.models.structure_type import StructureType
from app.persistence.structure_type_repository import StructureTypeRepository


def create_structure_types():
    struct_type_repo = StructureTypeRepository()
    data = [
        {'name': 'Ecole primaire', 'is_school': True},
        {'name': 'Collège', 'is_school': True},
        {'name': 'Lycée', 'is_school': True},
        {'name': 'Bibliothèque et médiathèques', 'is_school': False},
        {'name': 'Centre de loisirs', 'is_school': False},
        {'name': 'Foyer rural', 'is_school': False}
    ]
    for element in data:
        check_struct = struct_type_repo.get_by_attribute(
            'name', element['name'])
        if len(check_struct) == 0:
            struct = StructureType(**element)
            struct_type_repo.add(struct)
