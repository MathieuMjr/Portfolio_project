from app.persistence.structure_type_repository import StructureTypeRepository
from app.persistence.structure_repository import StructureRepository
from app.models.structure import Structure
from app.validators.structure import StructurePaylaod
from app.services.utils import (check_id, check_unique)


class StructureService():
    def __init__(self):
        self.structT_repo = StructureTypeRepository()
        self.struct_repo = StructureRepository()

    def create_struct(self, payload):
        # Payload validation with Pydantic
        valid_payload = StructurePaylaod(**payload).model_dump()

        # Check name uniqueness
        check_unique(
            'Structure', 'name', valid_payload['name'], self.struct_repo)

        # Check existing structure_type id
        struct_type_id = valid_payload['structure_type_id']
        check_id('Structure type', struct_type_id, self.structT_repo)

        # Create and save structure
        new_struct = Structure(**valid_payload)
        self.struct_repo.add(new_struct)

        return new_struct.to_dict()
