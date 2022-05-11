from typing import Optional
from pydantic import BaseModel

from .form_element_option import FormElementOption


# Shared properties
class SelectedListValueBase(BaseModel):
    selected_value_id: str
    form_element_option_id: str


# Properties to receive via API on creation
class SelectedListValueCreate(SelectedListValueBase):
    pass


# Properties to receive via API on update
class SelectedListValueUpdate(BaseModel):
    pass


class SelectedListValueInDBBase(SelectedListValueBase):
    form_element_option: FormElementOption
    class Config:
        orm_mode = True


# Additional properties to return via API
class SelectedListValue(SelectedListValueInDBBase):
    pass
