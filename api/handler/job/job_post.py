from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db_config import get_async_session
from schema.job_post_schema import JobPostCreate, JobPostPageRequest, JobPostResponse
from service.job_service import JobService

job_post_router = APIRouter()


@job_post_router.get("/get", response_model=List[JobPostResponse])
async def get_job_post_page(
    jop_post_page_request: JobPostPageRequest,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).get_job_post_page(jop_post_page_request=jop_post_page_request)
    return res


@job_post_router.post("/create", response_model=JobPostResponse)
async def create_job_post(
    job_post_create: JobPostCreate,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).create_job_post(job_post_create=job_post_create)
    await session.commit()
    return res


@job_post_router.post("/update", response_model=JobPostResponse)
async def update_job_post(
    job_post_create: JobPostCreate,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).update_job_post(job_post_create=job_post_create)
    await session.commit()
    return res


@job_post_router.delete("/delete", response_model=JobPostResponse)
async def delete_job_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).delete_job_post(post_id=post_id)
    await session.commit()
    return res
