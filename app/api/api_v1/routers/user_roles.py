from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, exceptions, models, crud
from app.api import deps

router = APIRouter(prefix="/user-roles", tags=["user-roles"])


# @router.get("/role/{user_id}", response_model=List[schemas.UserRole])
# async def read_user_roles(
#     # TODO star
#     *,
#     user_id: str,
#     db: Session = Depends(deps.get_db),
#     user: models.User = Security(
#         deps.get_current_active_user,
#         scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
#     ),
# ) -> any:
#     if user is None:
#         raise exceptions.get_user_exception()
#     """
#     Retrieve all user_roles.
#     """
#     return crud.user_role.get_by_user_id(db, user_id=user_id)


@router.post("", response_model=schemas.UserRole)
def assign_user_role(
    *,
    db: Session = Depends(deps.get_db),
    user_role_in: schemas.UserRoleCreate,
    current_user: models.User = Depends(
        deps.get_current_active_user
    ),
) -> Any:
    """
    Assign a role to a user after creation of a user
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    user_role = crud.user_role.get_by_user_id(
        db, user_id=user_role_in.user_id
    )
    if user_role:
        raise HTTPException(
            status_code=409,
            detail="This user has already been assigned a role.",
        )
    user_role = crud.user_role.create(db, obj_in=user_role_in)
    return user_role
