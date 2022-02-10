from datetime import timedelta

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import exceptions, crud
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db),
):
    user = crud.user.authenticate(
        form_data.username, form_data.password, db
    )
    if not user:
        raise exceptions.token_exception()
    # return "User validated"
    # return settings.SECRET_KEY
    token_expires = timedelta(minutes=20)
    token = security.create_access_token(
        user.email, user.id, expires_delta=token_expires
    )
    return {
        "token": token
    }
