from typing import Optional
from pydantic import BaseModel

from .form_element_list_value import FormElementListValue


# Shared properties
class SelectedListValueBase(BaseModel):
    filled_form_id: str
    form_element_list_value_id: str


# Properties to receive via API on creation
class SelectedListValueCreate(SelectedListValueBase):
    pass


# Properties to receive via API on update
class SelectedListValueUpdate(BaseModel):
    pass


class SelectedListValueInDBBase(SelectedListValueBase):
    form_element_list_value: FormElementListValue
    class Config:
        orm_mode = True


# Additional properties to return via API
class SelectedListValue(SelectedListValueInDBBase):
    pass
