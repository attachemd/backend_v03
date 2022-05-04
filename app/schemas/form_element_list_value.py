from typing import Optional
from pydantic import BaseModel


# Shared properties
class FormElementListValueBase(BaseModel):
    name: str
    form_element_field_id: str


# Properties to receive via API on creation
class FormElementListValueCreate(FormElementListValueBase):
    pass

class FormElementListValueCreateForRoute(BaseModel):
    name: str
    # form_element_field_id: str


# Properties to receive via API on update
class FormElementListValueUpdate(BaseModel):
    pass


class FormElementListValueInDBBase(FormElementListValueBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementListValue(FormElementListValueInDBBase):
    pass
