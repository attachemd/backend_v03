from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from schemas import UserDisplay, UserBase

router = APIRouter(prefix="/user", tags=["user"])


# Create user
@router.post("/", response_model=UserDisplay)
async def create_user(
    request: UserBase, db: Session = Depends(get_db)
):
    return db_user.create_user(db, request)
