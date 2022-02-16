from datetime import datetime
from enum import Enum
from typing import Optional

import pydantic
from pydantic import BaseModel

# from .custom_license import CustomLicense


class LicenseType(str, Enum):
    SIMPLE = "SIMPLE"
    CUSTOM = "CUSTOM"


# Shared properties
class LicenseBase(BaseModel):
    name: Optional[str]
    key: Optional[str]
    description: Optional[str]
    type: LicenseType = None

    # @pydantic.validator('type', pre=True)
    # def validate_enum_field(cls, type: str):
    #     return LicenseType(type)


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
    pass


class LicenseInDB(LicenseInDBBase):
    pass
