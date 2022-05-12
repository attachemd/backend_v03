from typing import Dict, List, Optional
from pydantic import BaseModel

from .selected_list_value import SelectedListValueCreate

from .selected_value import SelectedValueCreate

from .validation import Validation

from .form_element_option import FormElementOption, FormElementOptionCreateForRoute

from .form_element_template import FormElementTemplate, FormElementTemplateCreateForRoute


# Shared properties
class FormElementFieldBase(BaseModel):
    name: str
    form_element_template_id: Optional[str]
    form_id: Optional[str]


# Properties to receive via API on creation
class FormElementFieldCreate(FormElementFieldBase):
    pass

class FormElementFieldCreateForRoute(BaseModel):
    # id: str
    name: str
    form_element_template: FormElementTemplateCreateForRoute
    form_element_options: Optional[List[FormElementOptionCreateForRoute]]
    # selected_value: Optional[SelectedValueCreate]
    # selected_list_values: Optional[List[SelectedListValueCreate]]
    selected_value: str
    selected_list_value: Dict[str, bool]


# Properties to receive via API on update
class FormElementFieldUpdate(BaseModel):
    pass


class FormElementFieldInDBBase(FormElementFieldBase):
    id: str
    form_element_template: FormElementTemplate
    form_element_options: List[FormElementOption]
    field_validations_overriding: List[Validation]
    selected_value: Optional[SelectedValueCreate]
    # selected_list_values: Optional[SelectedListValueCreate]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementField(FormElementFieldInDBBase):
    pass
