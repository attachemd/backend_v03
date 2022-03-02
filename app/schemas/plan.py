from typing import Optional
from pydantic import BaseModel


# Shared properties
class PlanBase(BaseModel):
    product_id: Optional[str]
    account_id: Optional[str]


# Properties to receive via API on creation
class PlanCreate(PlanBase):
    pass


# Properties to receive via API on update
class PlanUpdate(BaseModel):
    pass


class PlanInDBBase(PlanBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class Plan(PlanInDBBase):
    pass
