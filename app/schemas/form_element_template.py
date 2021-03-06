from typing import List, Optional
from pydantic import BaseModel

from .validation import Validation

from .form_element_option import FormElementOption, FormElementOptionCreateForRoute

from .form_element_type import FormElementType


# Shared properties
class FormElementTemplateBase(BaseModel):
    name: str
    description: str
    form_element_type_id: str


# Properties to receive via API on creation
class FormElementTemplateCreate(FormElementTemplateBase):
    pass

class FormElementTemplateCreateForRoute(BaseModel):
    id: str
    # form_element_options: List[FormElementOptionCreateForRoute]


# Properties to receive via API on update
class FormElementTemplateUpdate(BaseModel):
    pass


class FormElementTemplateInDBBase(FormElementTemplateBase):
    id: str
    form_element_type: FormElementType
    # form_element_options: List[FormElementOption]
    validations: List[Validation]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementTemplate(FormElementTemplateInDBBase):
    pass
