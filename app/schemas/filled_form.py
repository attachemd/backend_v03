from pydantic import BaseModel


# Shared properties
class FilledFormBase(BaseModel):
    pass


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
