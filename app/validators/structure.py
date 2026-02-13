from pydantic import BaseModel, EmailStr, Field


class StructurePaylaod(BaseModel):
    name: str = Field(min_length=1)
    phone: str = Field(min_length=10, max_length=10)
    email: EmailStr
    zip_code: str = Field(min_length=5, max_length=5)
    address: str = Field(min_length=1)
    town: str = Field(min_length=1)
    structure_type_id: str = Field(min_length=1)
