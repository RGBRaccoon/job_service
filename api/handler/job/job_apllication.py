from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db_config import get_async_session
from model.user_model import UserModel
from schema.job_application_schema import JobApplicationCreate, JobApplicationResponse
from service.job_service import JobService
from api.handler.user.user_manager import current_active_user

job_application_router = APIRouter()


@job_application_router.post("/apply")
async def apply(
    job_appication_create: JobApplicationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: UserModel = Depends(current_active_user),
):
    res = await JobService(session=session).job_apply(job_appication_create=job_appication_create)
    await session.commit()
    return res


# @job_application_router.post("/bookmark")
# async def bookmark():
#     pass


@job_application_router.post("/cancel")
async def cancel(
    application_id: str,
    session: AsyncSession = Depends(get_async_session),
    user: UserModel = Depends(),
):
    res = await JobService(session=session).job_application_cancel(application_id=application_id)
    await session.commit()
    return res


@job_application_router.post("/get/my_apply", response_model=List[JobApplicationResponse])
async def get_my_apply(
    session: AsyncSession = Depends(get_async_session),
    user: UserModel = Depends(),
):
    res = await JobService(session=session).get_my_application(user_id=user.id)
    return res
