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
    # return "User validated"
    if not user:
        raise exceptions.token_exception()
    # return settings.SECRET_KEY
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    role = (
        "GUEST" if not user.user_role else user.user_role.role.name
    )
    token_payload = {
        "id": str(user.id),
        "role": role,
        "account_id": str(user.account_id),
    }
    token_dict = {
        "access": security.create_access_token(
            token_payload, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
    return schemas.Token(**token_dict)


# @router.post("/access_token")
# def login_for_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(deps.get_db),
#     Authorize: AuthJWT = Depends(),
# ):
#     """
#     Get an access token for future requests
#     """
#     user = crud.user.authenticate(
#         form_data.username, form_data.password, db
#     )

#     if not user:
#         raise exceptions.token_exception()

#     access_token_expires = timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#     )

#     role = (
#         "GUEST" if not user.user_role else user.user_role.role.name
#     )
#     user_claims = {
#         "id": str(user.id),
#         "role": role,
#         "account_id": str(user.account_id),
#     }
#     access_token = Authorize.create_access_token(
#         subject=str(user.id),
#         user_claims=user_claims,
#         expires_time=access_token_expires,
#     )
#     refresh_token = Authorize.create_refresh_token(
#         subject=str(user.id)
#     )
#     token_dict = {
#         "access": access_token,
#         "refresh": refresh_token,
#     }
#     return schemas.Token(**token_dict)

# @router.post('/refresh')
# def refresh(Authorize: AuthJWT = Depends()):
#     """
#     Refresh the access token for future requests
#     """
#     Authorize.jwt_refresh_token_required()

#     current_user = Authorize.get_jwt_subject()
#     new_access_token = Authorize.create_access_token(subject=current_user)
#     return {"access": new_access_token}

@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    """
    Refresh the access token for future requests
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access": new_access_token}
