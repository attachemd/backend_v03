from typing import List, Optional
from pydantic import BaseModel

from .validation import Validation

from .form_element_list_value import FormElementListValue, FormElementListValueCreateForRoute

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
    id: str
    name: str
    form_element_template: FormElementTemplateCreateForRoute
    form_element_list_values: List[FormElementListValueCreateForRoute]


# Properties to receive via API on update
class FormElementFieldUpdate(BaseModel):
    pass


class FormElementFieldInDBBase(FormElementFieldBase):
    id: str
    form_element_template: FormElementTemplate
    form_element_list_values: List[FormElementListValue]
    field_validations_overriding: List[Validation]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementField(FormElementFieldInDBBase):
    pass
