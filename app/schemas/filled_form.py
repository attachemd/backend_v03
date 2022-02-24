from typing import Optional
from pydantic import BaseModel


# Shared properties
class FilledFormBase(BaseModel):
    form_element_id: str
    value: Optional[str]


# Properties to receive via API on creation
class FilledFormCreate(FilledFormBase):
    pass


# Properties to receive via API on update
class FilledFormUpdate(BaseModel):
    pass


class FilledFormInDBBase(FilledFormBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class FilledForm(FilledFormInDBBase):
    pass
