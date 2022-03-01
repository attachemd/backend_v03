from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from app.api.api_v1.api import api_router
# from pydantic import BaseModel
# from app.core.config import settings
from app import schemas

from app.db import session, base_class

app = FastAPI()

# class AuthJwtSettings(BaseModel):
#     authjwt_secret_key: str = settings.SECRET_KEY

@AuthJWT.load_config
def get_config():
    return schemas.AuthJwtSettings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(api_router)


# ANCHOR[id=index]
# LINK todo#Formatting
@app.get("/hello")
async def index():
    return {"message": "Hello world!"}


base_class.Base.metadata.create_all(session.engine)
