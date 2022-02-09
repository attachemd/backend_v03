from typing import Optional

from pydantic import BaseModel, UUID4


# Shared properties
from app.schemas.role import Role


class UserRoleBase(BaseModel):
    user_id: Optional[UUID4]
    role_id: Optional[UUID4]


class UserRoleInDBBase(UserRoleBase):
    role: Role

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserRole(UserRoleInDBBase):
    pass
