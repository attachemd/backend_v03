from pydantic import BaseModel


# Shared properties
class SelectedFormElementListValueBase(BaseModel):
    pass


# Properties to receive via API on creation
class SelectedFormElementListValueCreate(SelectedFormElementListValueBase):
    pass


# Properties to receive via API on update
class SelectedFormElementListValueUpdate(BaseModel):
    pass


class SelectedFormElementListValueInDBBase(SelectedFormElementListValueBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class SelectedFormElementListValue(SelectedFormElementListValueInDBBase):
    pass
