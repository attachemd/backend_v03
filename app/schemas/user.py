from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, UUID4
from .user_role import UserRole
from .role import Role



# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None
    phone_number: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    user_roles: List[UserRole]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserWithRole(UserInDBBase):
    roles: List[Role]


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
