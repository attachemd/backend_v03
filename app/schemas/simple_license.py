from pydantic import BaseModel


# Shared properties
class SimpleLicenseBase(BaseModel):
    pass


# Properties to receive via API on creation
class SimpleLicenseCreate(SimpleLicenseBase):
    pass


# Properties to receive via API on update
class SimpleLicenseUpdate(BaseModel):
    pass


class SimpleLicenseInDBBase(SimpleLicenseBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class SimpleLicense(SimpleLicenseInDBBase):
    pass
