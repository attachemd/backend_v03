from enum import Enum
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    role: str
    password: str


class Role(str, Enum):
    admin = "admin"
    manager = "manager"


class UserDisplay(BaseModel):
    username: str
    email: str
    role: Role

    class Config:
        orm_mode = True
