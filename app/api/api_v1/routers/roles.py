from typing import List, Any

from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, exceptions, crud
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/roles", tags=["roles"])


@router.post("/", response_model=schemas.Role)
def create_role(
    *,
    db: Session = Depends(deps.get_db),
    role_in: schemas.Role,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Create new role.
    """
    if current_user is None:
        raise exceptions.get_user_exception()

    return crud.role.create(db, obj_in=role_in)


@router.get("/", response_model=List[schemas.Role])
async def get_roles(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve all available user roles.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.role.get_multi(db)
