from fastapi import APIRouter

from api.router.job_router import job_router
from api.router.user_router import user_router


api_router = APIRouter()


api_router.include_router(router=job_router, prefix="/job")
api_router.include_router(router=user_router, prefix="/auth", tags=["auth"])
