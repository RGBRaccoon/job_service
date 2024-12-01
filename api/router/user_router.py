from fastapi import APIRouter

from schema.user_schema import UserCreate, UserRead, UserUpdate
from api.handler.user.user_manager import auth_backend, fastapi_users

user_router = APIRouter()


user_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/register",
)
user_router.include_router(
    fastapi_users.get_reset_password_router(),
)
user_router.include_router(
    fastapi_users.get_verify_router(UserRead),
)
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
