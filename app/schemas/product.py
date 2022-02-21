from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    name: str


# Properties to receive via API on creation
class ProductCreate(ProductBase):
    pass


# Properties to receive via API on update
class ProductUpdate(BaseModel):
    pass


class ProductInDBBase(ProductBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class Product(ProductInDBBase):
    pass
