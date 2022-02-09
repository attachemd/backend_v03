from fastapi import FastAPI

from app.api import deps
from app.api.api_v1.api import api_router

# from app.api import user

app = FastAPI()

app.include_router(api_router)


@app.get("/hello")
async def index():
    return {"message": "Hello world!"}


deps.Base.metadata.create_all(deps.engine)
