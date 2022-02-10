from typing import Any

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud, exceptions

# from app.db import db_user
# from app.db.database import get_db
from app.api import deps

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def index(user: dict = Depends(deps.get_current_user)):
    if user is None:
        raise exceptions.get_user_exception()
    return {"message": "Hello world!"}


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
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user
