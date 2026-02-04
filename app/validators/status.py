from pydantic import BaseModel


class StatusValidator(BaseModel):
    name: str
