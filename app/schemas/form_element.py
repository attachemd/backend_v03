from pydantic import BaseModel


# Shared properties
class FormElementBase(BaseModel):
    pass


# Properties to receive via API on creation
class FormElementCreate(FormElementBase):
    pass


# Properties to receive via API on update
class FormElementUpdate(BaseModel):
    pass


class FormElementInDBBase(FormElementBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class FormElement(FormElementInDBBase):
    pass
