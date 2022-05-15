from typing import List, Optional

from pydantic import BaseModel

from .form_element_template import FormElementTemplate

from .selected_list_value import SelectedListValue


# Shared properties
class SelectedValueBase(BaseModel):
    form_element_field_id: str
    # client_id: str
    value: Optional[str]


# Properties to receive via API on creation
class SelectedValueCreate(SelectedValueBase):
    pass


# Properties to receive via API on update
class SelectedValueUpdate(BaseModel):
    pass


class SelectedValueInDBBase(SelectedValueBase):
    # selected_list_values: List[SelectedListValue]
    # form_element_template: FormElementTemplate
    class Config:
        orm_mode = True


# Additional properties to return via API
class SelectedValue(SelectedValueInDBBase):
    pass
