from pydantic import BaseModel, Field


class AudienceTypeValidator(BaseModel):
    name: str = Field(min_length=1)
    is_school: bool
