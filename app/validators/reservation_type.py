from pydantic import BaseModel, Field


class ReservationTypeValidator(BaseModel):
    name: str = Field(min_length=1)
