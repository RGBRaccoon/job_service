# 지원 관련 API
# 지원하기 API
# 관심 등록 API
# 지원 취소 API
# 지원 내역 조회 API


from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db_config import get_async_session
from model.user_model import UserModel
from schema.job_application_schema import JobApplicationCreate

job_application_router = APIRouter()


@job_application_router.post("/apply")
async def apply(
    job_appication: JobApplicationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: UserModel = Depends(),
):
    return True


@job_application_router.post("/bookmark")
async def bookmark():
    pass


@job_application_router.post("/cancel")
async def cancel():
    pass


@job_application_router.post("/get/my_apply")
async def get_my_apply():
    pass
