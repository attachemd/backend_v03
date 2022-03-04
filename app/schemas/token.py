from pydantic import BaseModel
from app.core.config import settings

class Token(BaseModel):
    access: str
    # refresh: str
    # token_type: str


# TODO
class TokenPayload(BaseModel):
    id: str
    role: str = None

class AuthJwtSettings(BaseModel):
    authjwt_secret_key: str = settings.SECRET_KEY