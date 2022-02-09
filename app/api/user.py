from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.db import db_user
from app.db.database import get_db
from app.schemas import UserDisplay, UserBase

router = APIRouter(prefix="/user", tags=["user"])


# Create user
@router.post("/", response_model=UserDisplay)
async def create_user(
    request: UserBase, db: Session = Depends(get_db)
):
    return db_user.create_user(db, request)
