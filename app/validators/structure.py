from pydantic import BaseModel, EmailStr
from app.models.structure_type import StructureType


class StructurePaylaod(BaseModel):
    name: str
    phone: str
    email: EmailStr
    zip_code: str
    address: str
    town: str
    structure_type_id: str


class StructureCreation(BaseModel):
    name: str
    phone: str
    email: EmailStr
    zip_code: str
    address: str
    town: str
    structure_type: StructureType
