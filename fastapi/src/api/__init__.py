from fastapi import APIRouter

from .routes import (
    notes_router,
    users_router,
)

api_router = APIRouter()
api_router.include_router(
    router=notes_router,
    prefix="/notes",
)
api_router.include_router(
    router=users_router,
    prefix="",
)
