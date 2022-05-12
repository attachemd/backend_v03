from typing import List, Optional
from pydantic import BaseModel

from .form_element_input_type import FormElementInputType


# Shared properties
class FormElementTypeBase(BaseModel):
    name: str
    # form_element_input_type_id: Optional[str]
    input_type: Optional[str]


# Properties to receive via API on creation
class FormElementTypeCreate(FormElementTypeBase):
    pass


# Properties to receive via API on update
class FormElementTypeUpdate(BaseModel):
    pass


class FormElementTypeInDBBase(FormElementTypeBase):
    # form_element_input_type: List[FormElementInputType]
    # form_element_input_type: Optional[FormElementInputType]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementType(FormElementTypeInDBBase):
    pass
