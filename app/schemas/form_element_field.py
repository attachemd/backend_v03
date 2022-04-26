from typing import Optional
from pydantic import BaseModel

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
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementField(FormElementFieldInDBBase):
    pass
