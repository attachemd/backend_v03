from typing import Optional
from pydantic import BaseModel


# Shared properties
class ElementFormMTMBase(BaseModel):
    form_element_id: Optional[str]
    form_id: Optional[str]


# Properties to receive via API on creation
class ElementFormMTMCreate(ElementFormMTMBase):
    pass


# Properties to receive via API on update
class ElementFormMTMUpdate(BaseModel):
    pass


class ElementFormMTMInDBBase(ElementFormMTMBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ElementFormMTM(ElementFormMTMInDBBase):
    pass
