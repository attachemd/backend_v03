from app.crud.crud_base import CRUDBase
from app.models.product import Product
from app.schemas import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    pass


product = CRUDProduct(Product)
