from typing import Optional

from pydantic import BaseModel


# Shared properties
class CustomLicenseBase(BaseModel):
    license_id: Optional[str]
    form_id: Optional[str]


# Properties to receive via API on creation
class CustomLicenseCreate(CustomLicenseBase):
    pass


# Properties to receive via API on update
class CustomLicenseUpdate(BaseModel):
    license_id: str


class CustomLicenseInDBBase(CustomLicenseBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class CustomLicense(CustomLicenseInDBBase):
    pass
