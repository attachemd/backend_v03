from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from app import schemas, exceptions, models, crud
from app.api import deps
from app.constants.role import Role

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


@router.post("/", response_model=schemas.UserRole)
def assign_user_role(
    *,
    db: Session = Depends(deps.get_db),
    user_role_in: schemas.UserRoleCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
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
    return crud.user_role.create(db, obj_in=user_role_in)


@router.put("/{user_id}/", response_model=schemas.UserRole)
def update_user_role(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    user_role_in: schemas.UserRoleUpdate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[
            Role.ADMIN["name"],
            Role.SUPER_ADMIN["name"],
            Role.ACCOUNT_ADMIN["name"],
        ],
    ),
) -> Any:
    """
    Update a users role.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    user_role = crud.user_role.get_by_user_id(db, user_id=user_id)
    if not user_role:
        raise HTTPException(
            status_code=404,
            detail="There is no role assigned to this user",
        )
    return crud.user_role.update(
        db, db_obj=user_role, obj_in=user_role_in
    )
