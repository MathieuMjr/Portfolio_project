from app.models.structure_type import StructureType
from app.persistence.structure_type_repository import StructureTypeRepository
import pytest
from sqlalchemy.exc import IntegrityError


def test_structure_type_creation(app, structure_type_data):
    repo = StructureTypeRepository()

    structureT = StructureType(**structure_type_data)
    repo.add(structureT)

    for key in structure_type_data:
        assert structure_type_data[key] == getattr(structureT, key)

    # TEST ALREADY EXISTING NAME

    structure2 = StructureType(**structure_type_data)

    with pytest.raises(IntegrityError):
        repo.add(structure2)


def test_bad_structure_type(app):
    repo = StructureTypeRepository()
    data = {'is_school': False}

    new_structure_type = StructureType(**data)

    with pytest.raises(IntegrityError):
        repo.add(new_structure_type)
