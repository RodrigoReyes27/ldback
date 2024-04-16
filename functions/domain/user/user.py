from uuid import uuid1, UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class User(BaseModel):

    model_config = ConfigDict(validate_assignment=True)

    id: UUID = Field(frozen=True)
    username: str = Field(min_length=5, max_length=30)
    email: EmailStr = Field()
    password: str = Field()
    root_directory_id: UUID = Field(alias="rootDirectoryId")

    @classmethod
    def create_new(
        cls, username: str, email: EmailStr, password: str, root_directory_id: UUID
    ) -> "User":
        return cls(
            id=uuid1(),
            username=username,
            email=email,
            password=password,
            rootDirectoryId=root_directory_id,
        )
