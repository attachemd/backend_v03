from typing import List, Optional
from pydantic import BaseModel

from .form_element_list_value import FormElementListValue

from .form_element_template import FormElementTemplate, FormElementTemplateCreateForRoute


# Shared properties
class FormElementFieldBase(BaseModel):
    label: str
    form_element_template_id: Optional[str]
    form_id: Optional[str]


# Properties to receive via API on creation
class FormElementFieldCreate(FormElementFieldBase):
    pass

class FormElementFieldCreateForRoute(BaseModel):
    label: str
    form_element_template: FormElementTemplateCreateForRoute


# Properties to receive via API on update
class FormElementFieldUpdate(BaseModel):
    pass


class FormElementFieldInDBBase(FormElementFieldBase):
    form_element_template: FormElementTemplate
    form_element_list_values: List[FormElementListValue]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementField(FormElementFieldInDBBase):
    pass
