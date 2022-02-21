from app.crud.crud_base import CRUDBase
from app.models.simple_license import SimpleLicense
from app.schemas import SimpleLicenseCreate, SimpleLicenseUpdate


class CRUDSimpleLicense(CRUDBase[SimpleLicense, SimpleLicenseCreate, SimpleLicenseUpdate]):
    pass


simple_license = CRUDSimpleLicense(SimpleLicense)
