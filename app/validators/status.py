from pydantic import BaseModel, Field


class StatusValidator(BaseModel):
    name: str = Field(min_length=1)
