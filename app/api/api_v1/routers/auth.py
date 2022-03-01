from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import exceptions, crud, schemas
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/access_token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db),
) -> schemas.Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        form_data.username, form_data.password, db
    )
    if not user:
        raise exceptions.token_exception()
    # return "User validated"
    # return settings.SECRET_KEY
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    role = (
        "GUEST" if not user.user_role else user.user_role.role.name
    )
    print(user.email)
    print(user.user_role)
    token_payload = {
        "id": str(user.id),
        "role": role,
        "account_id": str(user.account_id),
    }
    token_dict = {
        "access_token": security.create_access_token(
            token_payload, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
    return schemas.Token(**token_dict)


class User(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(user: User, Authorize: AuthJWT = Depends()):
    if user.username != "test" or user.password != "test":
        raise HTTPException(
            status_code=401, detail="Bad username or password"
        )
    another_claims = {"foo": ["fiz","baz"]}
    token_payload = {
        "id": str(user.username),
        "role": user.username,
        "account_id": str(user.username),
    }
    access_token = Authorize.create_access_token(
        subject=user.username, user_claims=token_payload
    )
    refresh_token = Authorize.create_refresh_token(
        subject=user.username
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
