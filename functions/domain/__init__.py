from pydantic import BaseModel, ConfigDict, Field


class AuthorizationModel(BaseModel):

    model_config = ConfigDict(frozen=True)

    user_id: str = Field()
    email: str = Field()
