from typing import Dict, List, Optional
from pydantic import BaseModel

from .selected_list_value import SelectedListValue

from .selected_value import SelectedValue

from .validation import Validation

from .form_element_option import FormElementOption, FormElementOptionCreateForRoute

from .form_element_template import FormElementTemplate, FormElementTemplateCreateForRoute


# Shared properties
class FormElementFieldBase(BaseModel):
    name: str
    form_element_template_id: Optional[str]
    form_id: Optional[str]
    sort_id: str


# Properties to receive via API on creation
class FormElementFieldCreate(FormElementFieldBase):
    pass

class FormElementFieldCreateForRoute(BaseModel):
    id: str
    name: str
    form_element_template: FormElementTemplateCreateForRoute
    form_element_options: Optional[List[FormElementOptionCreateForRoute]]
    # selected_value: Optional[SelectedValueCreate]
    # selected_list_values: Optional[List[SelectedListValueCreate]]
    selected_value: Optional[str]
    selected_list_value: Optional[Dict[str, bool]]
    state: Optional[str]
    sort_id: str


# Properties to receive via API on update
class FormElementFieldUpdate(BaseModel):
    pass


class FormElementFieldInDBBase(FormElementFieldBase):
    id: str
    form_element_template: FormElementTemplate
    form_element_options: List[FormElementOption]
    field_validations_overriding: List[Validation]
    selected_value: Optional[SelectedValue]
    selected_list_values: Optional[List[SelectedListValue]]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementField(FormElementFieldInDBBase):
    pass
