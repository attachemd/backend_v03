from pydantic import BaseModel


# Shared properties
class FormElementTypeBase(BaseModel):
    name: str


# Properties to receive via API on creation
class FormElementTypeCreate(FormElementTypeBase):
    pass


# Properties to receive via API on update
class FormElementTypeUpdate(BaseModel):
    pass


class FormElementTypeInDBBase(FormElementTypeBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElementType(FormElementTypeInDBBase):
    pass
