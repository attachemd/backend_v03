from typing import List, Optional

from pydantic import BaseModel

from .form_element import FormElement

from .selected_list_value import SelectedListValue


# Shared properties
class FilledFormBase(BaseModel):
    form_element_id: str
    account_id: str
    value: Optional[str]


# Properties to receive via API on creation
class FilledFormCreate(FilledFormBase):
    pass


# Properties to receive via API on update
class FilledFormUpdate(BaseModel):
    pass


class FilledFormInDBBase(FilledFormBase):
    selected_list_values: List[SelectedListValue]
    form_element: FormElement
    class Config:
        orm_mode = True


# Additional properties to return via API
class FilledForm(FilledFormInDBBase):
    pass
