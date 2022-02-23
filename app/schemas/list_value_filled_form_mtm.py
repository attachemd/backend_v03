from typing import Optional
from pydantic import BaseModel


# Shared properties
class ListValueFilledFormMTMBase(BaseModel):
    filled_form_id: str
    form_element_list_values_id: str


# Properties to receive via API on creation
class ListValueFilledFormMTMCreate(ListValueFilledFormMTMBase):
    pass


# Properties to receive via API on update
class ListValueFilledFormMTMUpdate(BaseModel):
    pass


class ListValueFilledFormMTMInDBBase(ListValueFilledFormMTMBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ListValueFilledFormMTM(ListValueFilledFormMTMInDBBase):
    pass
