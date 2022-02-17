from pydantic import BaseModel


# Shared properties
class FormElementListValueBase(BaseModel):
    pass


# Properties to receive via API on creation
class FormElementListValueCreate(FormElementListValueBase):
    pass


# Properties to receive via API on update
class FormElementListValueUpdate(BaseModel):
    pass


class FormElementListValueInDBBase(FormElementListValueBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementListValue(FormElementListValueInDBBase):
    pass
