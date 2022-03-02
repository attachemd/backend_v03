from typing import Generator

from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt, JWTError, ExpiredSignatureError
from jose.exceptions import JWTClaimsError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import exceptions, crud, schemas, models
from app.constants.role import Role
from app.core.config import settings

from app.db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_bearer = OAuth2PasswordBearer(
    tokenUrl="api/auth/access_token2",
    scopes={
        Role.GUEST["name"]: Role.GUEST["description"],
        Role.ACCOUNT_ADMIN["name"]: Role.ACCOUNT_ADMIN[
            "description"
        ],
        Role.ACCOUNT_MANAGER["name"]: Role.ACCOUNT_MANAGER[
            "description"
        ],
        Role.ADMIN["name"]: Role.ADMIN["description"],
        Role.SUPER_ADMIN["name"]: Role.SUPER_ADMIN["description"],
    },
)


# TODO
async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_bearer),
    db: Session = Depends(get_db),
) -> models.User:
    if security_scopes.scopes:
        authenticate_value = (
            f'Bearer scope="{security_scopes.scope_str}"'
        )
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload= jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        # email: str = payload.get("sub")
        # user_id: int = payload.get("id")
        if payload.get("id") is None:
            raise credentials_exception
        # return {"email": email, "id": user_id}
        token_data = schemas.TokenPayload(**payload)
    except (ValidationError, ExpiredSignatureError) as e:
        raise exceptions.get_user_exception(str(e))
    except JWTClaimsError as e:
        raise exceptions.get_user_exception(str(e))
    except JWTError as e:
        raise exceptions.get_user_exception(str(e))
    user = crud.user.get(db, obj_id=token_data.id)
    if not user:
        raise credentials_exception
    if security_scopes.scopes and not token_data.role:
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions with invalid token",
            headers={"WWW-Authenticate": authenticate_value},
        )
    if (
        security_scopes.scopes
        and token_data.role not in security_scopes.scopes
    ):
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )
    return user


def get_current_active_user(
    current_user: models.User = Security(
        get_current_user,
        scopes=[],
    ),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
