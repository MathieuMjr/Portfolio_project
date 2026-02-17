from pydantic import BaseModel, Field, ConfigDict


class StatusValidator(BaseModel):
    name: str = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')
