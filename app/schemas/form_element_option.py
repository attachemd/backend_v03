from typing import Optional
from pydantic import BaseModel

# from app.schemas.selected_list_value import SelectedListValue

# from .selected_list_value import SelectedListValue


# Shared properties
class FormElementOptionBase(BaseModel):
    id: Optional[str]
    name: str
    form_element_field_id: str


# Properties to receive via API on creation
class FormElementOptionCreate(FormElementOptionBase):
    pass


class FormElementOptionCreateForRoute(BaseModel):
    id: Optional[str]
    name: str
    # form_element_field_id: str


# Properties to receive via API on update
class FormElementOptionUpdate(BaseModel):
    pass


class FormElementOptionInDBBase(FormElementOptionBase):
    # selected_option_value: Optional[SelectedListValue]
    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementOption(FormElementOptionInDBBase):
    pass
