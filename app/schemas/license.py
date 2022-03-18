from datetime import date, datetime
from enum import Enum
from typing import Optional, Literal
from pydantic import BaseModel

from .client import Client

from .product import Product

from .custom_license import CustomLicense


class LicenseType(str, Enum):
    SIMPLE = "SIMPLE"
    CUSTOM = "CUSTOM"


# Shared properties
class LicenseBase(BaseModel):
    # name: Optional[str]
    key: Optional[str]
    description: Optional[str]
    type: LicenseType
    # expiry: date
    status: bool = False
    expiry: datetime
    product_id: str
    client_id: str

    # type: # Literal["SIMPLE1", "CUSTOM2"]

    # @pydantic.validator('type', pre=True)
    # def validate_enum_field(cls, type: str):
    #     return LicenseType(type)

# https://stackoverflow.com/q/66570894       
class FlatLicenseDict(BaseModel):
    client: str
    def __init__(self, **kwargs):
        kwargs["client"] = kwargs["client"]["first_name"] + " " + kwargs["client"]["last_name"]
        super().__init__(**kwargs)
        
class FlatLicense(BaseModel):
    client: str
    
# Properties to receive via API on creation
class LicenseCreate(LicenseBase):
    pass


# Properties to receive via API on update
class LicenseUpdate(LicenseBase):
    pass


class LicenseInDBBase(LicenseBase):
    id: str
    created_at: datetime
    updated_at: datetime
    # custom_license: CustomLicense

    class Config:
        orm_mode = True
        use_enum_values = True


# Additional properties to return via API
class License(LicenseInDBBase):
    product: Product
    client: Client


class LicenseInDB(LicenseInDBBase):
    pass
