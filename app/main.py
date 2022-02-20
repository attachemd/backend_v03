from fastapi import FastAPI

from app.api.api_v1.api import api_router

from app.db import session, base_class

app = FastAPI()

app.include_router(api_router)


# ANCHOR[id=index]
# LINK todo#Formatting
@app.get("/hello")
async def index():
    return {"message": "Hello world!"}


base_class.Base.metadata.create_all(session.engine)
