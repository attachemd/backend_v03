from black import List
from pydantic import BaseModel
from app.core.config import settings


class Token(BaseModel):
    access: str
    # refresh: str
    # token_type: str


class RoleForToken(BaseModel):
    name: str


# TODO
class TokenPayload(BaseModel):
    id: str
    roles: List[RoleForToken] = None


class AuthJwtSettings(BaseModel):
    authjwt_secret_key: str = settings.SECRET_KEY
