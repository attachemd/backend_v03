from typing import Optional

from pydantic import BaseModel


# Shared properties
class ValidationBase(BaseModel):
    message: str
    validator_id: str
    form_element_template_id: Optional[str]
    form_element_field_id: Optional[str]
    pattern: Optional[str]


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
