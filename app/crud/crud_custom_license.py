from typing import Optional

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.custom_license import CustomLicense
from app.schemas import CustomLicenseCreate, CustomLicenseUpdate


class CRUDCustomLicense(
    CRUDBase[CustomLicense, CustomLicenseCreate, CustomLicenseUpdate]
):
    def get_by_license_id(
        self, db: Session, *, license_id: str
    ) -> Optional[CustomLicense]:
        return (
            db.query(CustomLicense)
            .filter(CustomLicense.license_id == license_id)
            .first()
        )


custom_license = CRUDCustomLicense(CustomLicense)
