from fastapi import APIRouter

from app.api.api_v1.routers import users, auth, roles, user_roles

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(roles.router)
api_router.include_router(user_roles.router)
