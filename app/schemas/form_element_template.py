from typing import Optional
from pydantic import BaseModel

from .form_element import FormElement


# Shared properties
class FormElementTemplateBase(BaseModel):
    form_element_id: Optional[str]
    form_id: Optional[str]


# Properties to receive via API on creation
class FormElementTemplateCreate(FormElementTemplateBase):
    pass


# Properties to receive via API on update
class FormElementTemplateUpdate(BaseModel):
    pass


class FormElementTemplateInDBBase(FormElementTemplateBase):
    form_element: FormElement
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementTemplate(FormElementTemplateInDBBase):
    pass
