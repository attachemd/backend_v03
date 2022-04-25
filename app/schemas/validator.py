from typing import Optional

from pydantic import BaseModel


# Shared properties
class ValidatorBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


# Properties to receive via API on creation
class ValidatorCreate(ValidatorBase):
    pass


# Properties to receive via API on update
class ValidatorUpdate(ValidatorBase):
    pass


class ValidatorInDBBase(ValidatorBase):
    # id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class Validator(ValidatorInDBBase):
    pass
