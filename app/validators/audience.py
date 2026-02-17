from pydantic import BaseModel, Field, ConfigDict


class AudiencePayload(BaseModel):
    count: int = Field(gt=0)
    # validateur de count positif
    audience_type_id: str = Field(min_length=1)
    reservation_id: str = Field(min_length=1)

    model_config = ConfigDict(extra='forbid')
