

from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated


class UserBase(BaseModel):
    full_name: str
    username: Annotated[str, Field(min_length=8, max_length=255)]


class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=8, max_length=255)]


class UserLogin(BaseModel):
    username: Annotated[str, Field(min_length=8, max_length=255)]
    password: Annotated[str, Field(min_length=8, max_length=255)]


class ChangePassword(BaseModel):
    id: int
    new_password: Annotated[str, Field(min_length=8, max_length=255)]


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
