from typing import Any, List

from fastapi import Depends, APIRouter, HTTPException, Security
from sqlalchemy.orm import Session

from app import schemas, crud, exceptions, models

# from app.db import db_user
# from app.db.database import get_db
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[schemas.User])
async def read_users(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve all users.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.user.get_multi(db)


# Create user
# @router.post("/", response_model=schemas.User)
# async def create_user(
#     request: UserBase, db: Session = Depends(get_db)
# ):
#     return db_user.create_user(db, request)


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    # TODO UNIQUE constraint failed: users.phone_number
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.get("/me/", response_model=schemas.User)
# @router.get("/me/")
def get_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(
        deps.get_current_active_user
    ),
) -> Any:
    """
    Get current user.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    # role = (
    #     None
    #     if not current_user.user_role
    #     else current_user.user_role.role.name
    # )
    # return schemas.User(
    #     id=current_user.id,
    #     email=current_user.email,
    #     is_active=current_user.is_active,
    #     full_name=current_user.full_name,
    #     created_at=current_user.created_at,
    #     updated_at=current_user.updated_at,
    #     role=role,
    # )
    return current_user
