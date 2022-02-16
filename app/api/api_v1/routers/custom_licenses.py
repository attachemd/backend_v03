from typing import Any

from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, exceptions, crud
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/custom_licenses", tags=["custom_licenses"])


@router.post("/", response_model=schemas.CustomLicense)
def assign_custom_license(
    *,
    db: Session = Depends(deps.get_db),
    custom_license_in: schemas.CustomLicenseCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Assign a customization to a license.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    custom_license = crud.custom_license.get_by_license_id(
        db, license_id=custom_license_in.license_id
    )
    if custom_license:
        raise HTTPException(
            status_code=409,
            detail="This customization has already been assigned a license.",
        )
    return crud.custom_license.create(db, obj_in=custom_license_in)
