from pydantic import BaseModel, ConfigDict, Field

from ..user import User


class CreateUserCommand(BaseModel):
    model_config = ConfigDict(frozen=True)

    username: str = Field()
