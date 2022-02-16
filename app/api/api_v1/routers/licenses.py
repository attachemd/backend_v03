from typing import Any, List

from fastapi import Depends, APIRouter, HTTPException, Security, Body
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import schemas, crud, exceptions, models

# from app.db import db_user
# from app.db.database import get_db
from app.api import deps
from app.constants.role import Role
from app.core.config import settings
from app.models.account import Account

# from app.models.license import License
from app.models.user_role import UserRole

router = APIRouter(prefix="/licenses", tags=["licenses"])


@router.post("/")
def create_license(
    *,
    db: Session = Depends(deps.get_db),
    license_in: schemas.LicenseCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Create new license.
    """
    if current_user is None:
        raise exceptions.get_user_exception()

    return crud.license.create(db, obj_in=license_in)


# @router.get("/", response_model=List[schemas.License])
@router.get("/")
async def get_licenses(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve all licenses.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    # current_license = crud.license.get_multi2(db)
    # return schemas.License(
    #     id=current_license.id,
    #     name=current_license.name,
    #     key=current_license.key,
    #     description=current_license.description,
    #     type=current_license.type.value,
    # )
    return crud.license.get_multi(db)
