from typing import List
from pydantic import BaseModel

from .form_element_template import FormElementTemplate


# Shared properties
class FormBase(BaseModel):
    name: str


# Properties to receive via API on creation
class FormCreate(FormBase):
    pass


# Properties to receive via API on update
class FormUpdate(BaseModel):
    pass


class FormInDBBase(FormBase):
    form_element_templates: List[FormElementTemplate]
    class Config:
        orm_mode = True


# Additional properties to return via API
class Form(FormInDBBase):
    pass
