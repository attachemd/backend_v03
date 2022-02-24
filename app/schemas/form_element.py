from typing import List, Optional
from pydantic import BaseModel

from .form_element_list_value import FormElementListValue

from .form_element_type import FormElementType


# Shared properties
class FormElementBase(BaseModel):
    name: str
    form_element_type_id: Optional[str]


# Properties to receive via API on creation
class FormElementCreate(FormElementBase):
    pass


# Properties to receive via API on update
class FormElementUpdate(BaseModel):
    pass


class FormElementInDBBase(FormElementBase):
    form_element_type: FormElementType
    form_element_list_values: List[FormElementListValue]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElement(FormElementInDBBase):
    pass
