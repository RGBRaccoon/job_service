from fastapi import APIRouter
from api.handler.job.job_post import job_post_router
from api.handler.job.job_apllication import job_application_router

job_router = APIRouter()

job_router.include_router(router=job_post_router, prefix="/post", tags=["job_post"])
job_router.include_router(router=job_application_router, prefix="/apply", tags=["job_application"])
