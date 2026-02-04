from pydantic import BaseModel


class StructureTypeValidator(BaseModel):
    name: str
    is_school: bool
