from pydantic import ConfigDict, EmailStr, Field
from pydantic.main import BaseModel


class UserWrite(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str
    email: EmailStr


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: EmailStr


class UserResponseWithToken(BaseModel):
    access_token: str
    token_type: str
    user: UserRead
