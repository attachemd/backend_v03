from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4
from app.schemas.user_role import UserRole


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    account_id: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    user_role: Optional[UserRole]
    created_at: datetime
    updated_at: datetime
    role: Optional[str]

    class Config:
        orm_mode = True


class UserWithRole(UserInDBBase):
    role: Optional[str]


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
