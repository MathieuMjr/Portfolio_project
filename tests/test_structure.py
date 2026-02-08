from app.models.structure import Structure
from app.persistence.structure_repository import StructureRepository
from app.models.structure_type import StructureType
from app.persistence.structure_type_repository import StructureTypeRepository
import pytest
from sqlalchemy.exc import IntegrityError


def test_structure_creation(app, structure_type_data):
    structure_repo = StructureRepository()
    structureT_repo = StructureTypeRepository()
    st = StructureType(**structure_type_data)
    structureT_repo.add(st)

    data = {
        'name': 'Ecole Saint-Joseph',
        'phone': '0380403324',
        'email': 'ecole@st-jo.fr',
        'zip_code': '21000',
        'address': '2 rue du coquelicot',
        'town': 'Dijon',
        'structure_type_id': st.id
    }
    structure = Structure(**data)
    structure_repo.add(structure)

    for key in data:
        assert data[key] == getattr(structure, key)
    assert structure.structure_type_id == st.id
    assert structure.structure_type == st

    structure_2 = Structure(**data)
    with pytest.raises(IntegrityError):
        structure_repo.add(structure_2)


def test_bad_structure_creation(app, structure_type_data):
    structure_repo = StructureRepository()
    structureT_repo = StructureTypeRepository()
    st = StructureType(**structure_type_data)
    structureT_repo.add(st)

    data = {
        'name': 'Ecole Saint-Joseph',
        'phone': '0380403324',
        'email': 'ecole@st-jo.fr',
        'zip_code': '21000',
        'address': '2 rue du coquelicot',
        'town': 'Dijon',
    }
    structure = Structure(**data)

    with pytest.raises(IntegrityError):
        structure_repo.add(structure)
