from pydantic import BaseModel


class ReservationTypeValidator(BaseModel):
    name: str
