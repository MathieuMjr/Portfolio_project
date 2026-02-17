from pydantic import BaseModel, Field, ConfigDict


class ThemePayload(BaseModel):
    name: str = Field(min_length=1)
    reservation_type_id: str = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')
