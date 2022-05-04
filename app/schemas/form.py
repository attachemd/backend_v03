from typing import List
from pydantic import BaseModel

from .form_element_field import FormElementField, FormElementFieldCreateForRoute


# Shared properties
class FormBase(BaseModel):
    # name: str
    pass


# Properties to receive via API on creation
class FormCreate(FormBase):
    pass

class FormCreateForRoute(FormBase):
    form_element_fields: List[FormElementFieldCreateForRoute]
    pass


# Properties to receive via API on update
class FormUpdate(BaseModel):
    pass


class FormInDBBase(FormBase):
    form_element_fields: List[FormElementField]
    class Config:
        orm_mode = True


# Additional properties to return via API
class Form(FormInDBBase):
    pass
