from typing import List, Optional
from unicodedata import name

from pydantic import BaseModel
from .role import Role


# Shared properties
class UserRoleBase(BaseModel):
    user_id: Optional[str]
    role_id: Optional[str]


# Properties to receive via API on creation
class UserRoleCreate(UserRoleBase):
    pass


# Properties to receive via API on update
class UserRoleUpdate(BaseModel):
    role_id: str


class UserRoleInDBBase(UserRoleBase):
    role: Role

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserRole(UserRoleInDBBase):
    pass


# class UserRoleForToken(UserRoleInDBBase):
#     def __init__(self, **kwargs):
#         kwargs["name"] = kwargs["role"]["name"]
#         super().__init__(**kwargs)

# https://stackoverflow.com/q/66570894       
class UserRoleNameDict(BaseModel):
    name: str
    def __init__(self, **kwargs):
        kwargs["name"] = kwargs["role"]["name"]
        super().__init__(**kwargs)
        
class UserGroup(BaseModel):
    name: str
