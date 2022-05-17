from typing import List, Optional
from pydantic import BaseModel

from .form_element_field import FormElementField, FormElementFieldCreateForRoute


# Shared properties
class FormBase(BaseModel):
    id: Optional[str]
    # name: str
    pass


# Properties to receive via API on creation
class FormCreate(FormBase):
    pass

class FormCreateForRoute(FormBase):
    form_element_fields: List[FormElementFieldCreateForRoute]
    deleted_option_ids: List[str]
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
