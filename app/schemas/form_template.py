from typing import Optional
from pydantic import BaseModel

from .form_element import FormElement


# Shared properties
class FormTemplateBase(BaseModel):
    form_element_id: Optional[str]
    form_id: Optional[str]


# Properties to receive via API on creation
class FormTemplateCreate(FormTemplateBase):
    pass


# Properties to receive via API on update
class FormTemplateUpdate(BaseModel):
    pass


class FormTemplateInDBBase(FormTemplateBase):
    form_element: FormElement
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormTemplate(FormTemplateInDBBase):
    pass
