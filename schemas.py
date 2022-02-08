from enum import Enum
from typing import Literal

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    role: str
    password: str


class Role(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


class UserDisplay(BaseModel):
    username: str
    email: str
    role: Role = None
    # role: Literal["admin", "manager"]
    # role: Literal[Role.admin, Role.manager]

    class Config:
        orm_mode = True
