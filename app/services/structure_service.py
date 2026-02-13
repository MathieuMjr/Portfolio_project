from app.persistence.structure_type_repository import StructureTypeRepository
from app.persistence.structure_repository import StructureRepository
from app.models.structure import Structure
from app.validators.structure import StructurePaylaod


class StructureService():
    def __init__(self):
        self.structT_repo = StructureTypeRepository()
        self.struct_repo = StructureRepository()

    def create_struct(self, payload):
        # Payload validation with Pydantic
        valid_payload = StructurePaylaod(**payload).model_dump()

        # Check name uniqueness
        check_obj = self.struct_repo.get_by_attribute(
            'name', valid_payload['name'])
        if len(check_obj) != 0 and check_obj[0].is_active is False:
            raise ValueError(
                'Deactivated structure with this name already exists')
        if len(check_obj) != 0 and check_obj[0].is_active is True:
            raise ValueError('Structure with this name already exist')

        # Check existing structure_type id
        struct_type_id = valid_payload['structure_type_id']
        check_type = self.structT_repo.get_id(struct_type_id)
        if not check_type:
            raise LookupError(
                f'Structure type {struct_type_id} not found')
        if check_type.is_active is False:
            raise LookupError(
                f'Structure type {valid_payload['name']} is deactivated'
            )

        # Create and save structure
        new_struct = Structure(**valid_payload)
        self.struct_repo.add(new_struct)

        return new_struct.to_dict()
