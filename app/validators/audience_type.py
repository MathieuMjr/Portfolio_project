from pydantic import BaseModel


class AudienceTypeValidator(BaseModel):
    name: str
    is_school: bool
