from fastapi import FastAPI

from app import models, db
from app.api.api_v1.api import api_router

# from app.api import user
from app.db import session, base

app = FastAPI()

app.include_router(api_router)


@app.get("/hello")
async def index():
    return {"message": "Hello world!"}


base.Base.metadata.create_all(session.engine)
