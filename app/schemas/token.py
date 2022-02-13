from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


# TODO
class TokenPayload(BaseModel):
    id: str
    role: str = None
    account_id: str = None
