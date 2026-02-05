from pydantic import BaseModel, Field


class StructureTypeValidator(BaseModel):
    name: str = Field(min_length=1)
    is_school: bool
