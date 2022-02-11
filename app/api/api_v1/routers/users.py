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
    user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> any:
    if user is None:
        raise exceptions.get_user_exception()
    """
    Retrieve all users.
    """
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
