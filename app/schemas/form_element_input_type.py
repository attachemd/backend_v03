from typing import Optional

from pydantic import BaseModel


# Shared properties
class FormElementInputTypeBase(BaseModel):
    input_type: str
    form_element_type_id: str


# Properties to receive via API on creation
class FormElementInputTypeCreate(FormElementInputTypeBase):
    pass


# Properties to receive via API on update
class FormElementInputTypeUpdate(FormElementInputTypeBase):
    pass


class FormElementInputTypeInDBBase(FormElementInputTypeBase):
    # id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementInputType(FormElementInputTypeInDBBase):
    pass
