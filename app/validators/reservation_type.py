from pydantic import BaseModel, Field, ConfigDict


class ReservationTypeValidator(BaseModel):
    name: str = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')
