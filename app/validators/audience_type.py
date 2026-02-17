from pydantic import BaseModel, Field, ConfigDict


class AudienceTypeValidator(BaseModel):
    name: str = Field(min_length=1)
    is_school: bool

    model_config = ConfigDict(extra='forbid')
