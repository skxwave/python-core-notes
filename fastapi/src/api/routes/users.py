from fastapi import APIRouter

from src.schemas.users import UserRead, UserUpdate
from src.core.auth.transport import fastapi_users, auth_backend

router = APIRouter()

router.include_router(
    fastapi_users.get_register_router(UserRead, UserUpdate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
