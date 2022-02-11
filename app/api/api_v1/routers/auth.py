from datetime import timedelta

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
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
        "role": role
    }
    token_dict = {
        "access_token": security.create_access_token(
            token_payload, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
    return schemas.Token(**token_dict)
