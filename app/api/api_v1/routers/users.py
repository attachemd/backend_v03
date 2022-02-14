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
def create_user_by_admin(
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
    return crud.user.create(db, obj_in=user_in)


@router.get("/me/", response_model=schemas.UserWithRole)
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
    role = (
        None
        if not current_user.user_role
        else current_user.user_role.role.name
    )
    return schemas.UserWithRole(
        id=current_user.id,
        email=current_user.email,
        is_active=current_user.is_active,
        full_name=current_user.full_name,
        created_at=current_user.created_at,
        updated_at=current_user.updated_at,
        role=role,
    )
    # return current_user


@router.post("/open/", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(...),
    phone_number: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(
        password=password,
        email=email,
        full_name=full_name,
        phone_number=phone_number,
    )
    return crud.user.create(db, obj_in=user_in)


@router.get("/{user_id}/", response_model=schemas.User)
def get_user_by_id(
    user_id: str,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.user.get(db, obj_id=user_id)


@router.put("/{user_id}/", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    user_in: schemas.UserUpdate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Update a user.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    user = crud.user.get(db, obj_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    return crud.user.update(db, db_obj=user, obj_in=user_in)
