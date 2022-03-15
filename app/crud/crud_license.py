from typing import Optional

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.license import License
from app.schemas import LicenseCreate, LicenseUpdate


class CRUDLicense(CRUDBase[License, LicenseCreate, LicenseUpdate]):
    def create(self, db: Session, *, obj_in: LicenseCreate) -> License:
        db_obj = License(
            key=obj_in.key,
            description=obj_in.description,
            type=obj_in.type,
            expiry=obj_in.expiry,
            status=obj_in.status,
            product_id=obj_in.product_id,
            account_id=obj_in.account_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


license = CRUDLicense(License)
