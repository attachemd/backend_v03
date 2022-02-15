from typing import Optional

from pydantic import BaseModel
from app.schemas.role import Role


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
