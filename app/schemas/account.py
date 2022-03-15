from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class AccountBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    description: Optional[str]
    country: Optional[str]
    city: Optional[str]
    # current_subscription_ends: Optional[datetime]
    # plan_id: Optional[str]
    user_id: str
    is_active: Optional[bool] = True


# Properties to receive via API on creation
class AccountCreate(AccountBase):
    pass


# Properties to receive via API on update
class AccountUpdate(AccountBase):
    pass


class AccountInDBBase(AccountBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Account(AccountInDBBase):
    pass


class AccountInDB(AccountInDBBase):
    pass
