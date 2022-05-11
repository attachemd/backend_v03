from typing import Optional
from pydantic import BaseModel


# Shared properties
class FormElementOptionBase(BaseModel):
    name: str
    form_element_field_id: str


# Properties to receive via API on creation
class FormElementOptionCreate(FormElementOptionBase):
    pass

class FormElementOptionCreateForRoute(BaseModel):
    name: str
    # form_element_field_id: str


# Properties to receive via API on update
class FormElementOptionUpdate(BaseModel):
    pass


class FormElementOptionInDBBase(FormElementOptionBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementOption(FormElementOptionInDBBase):
    pass