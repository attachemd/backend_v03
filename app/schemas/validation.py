from typing import Optional

from pydantic import BaseModel


# Shared properties
class ValidationBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


# Properties to receive via API on creation
class ValidationCreate(ValidationBase):
    pass


# Properties to receive via API on update
class ValidationUpdate(ValidationBase):
    pass


class ValidationInDBBase(ValidationBase):
    # id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class Validation(ValidationInDBBase):
    pass
