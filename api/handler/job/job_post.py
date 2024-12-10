from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from config.db_config import get_async_session
from model.user_model import UserModel
from schema.job_post_schema import JobPostCreate, JobPostListResponse, JobPostPageRequest, JobPostResponse
from service.job_service import JobService
from api.handler.user.user_manager import current_active_user

job_post_router = APIRouter()


@job_post_router.get("/page", summary="채용 공고 검색. 필터링, 키워드 정렬.", response_model=JobPostListResponse)
async def get_job_post_page(
    jop_post_page_request: JobPostPageRequest,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).get_job_post_page(jop_post_page_request=jop_post_page_request)
    return res


@job_post_router.get("/get", summary="채용공고 하나 조회", response_model=JobPostResponse)
async def get_job_post_by_id(post_id: str, session: AsyncSession = Depends(get_async_session)):
    res = await JobService(session=session).get_job_post_by_id(post_id=post_id)
    return res


@job_post_router.post("/create", summary="채용공고 생성", response_model=JobPostResponse)
async def create_job_post(
    job_post_create: JobPostCreate,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).create_job_post(job_post_create=job_post_create)
    await session.commit()
    return res


@job_post_router.post("/update", summary="채용공고 수정", response_model=JobPostResponse)
async def update_job_post(
    post_id: str,
    job_post_create: JobPostCreate,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).update_job_post(post_id=post_id, job_post_create=job_post_create)
    await session.commit()
    return res


@job_post_router.delete("/delete", summary="채용공고 삭제")
async def delete_job_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session),
):
    res = await JobService(session=session).delete_job_post(post_id=post_id)
    await session.commit()
    return JSONResponse(content="post deleted. post_id : " + res, status_code=status.HTTP_200_OK)
    # return raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@job_post_router.post("/bookmark", summary="채용공고 찜", response_model=JobPostResponse)
async def bookmark_job_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session),
    user: UserModel = Depends(current_active_user),
):

    res = await JobService(session=session).bookmark_job_post(post_id=post_id, user_id=user.id)
    await session.commit()
    return res


@job_post_router.post("/get/my_bookmark", summary="내가 북마크한 채용공고 조회", response_model=JobPostResponse)
async def get_bookmark_job_post(
    session: AsyncSession = Depends(get_async_session),
    user: UserModel = Depends(current_active_user),
):
    # TODO : 필터링 기능 개선 필요. 위의 일반 공고 검색기능과 같은 필터링을 추가 할 것.
    res = await JobService(session=session).get_bookmark_job_post(user_id=user.id)
    return res
