from typing import Optional

from pydantic import BaseModel, UUID4


# Shared properties
class RoleBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


class RoleInDBBase(RoleBase):
    # id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class Role(RoleInDBBase):
    pass
