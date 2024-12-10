from typing import List
from uuid import UUID

from psycopg2 import DatabaseError
from sqlalchemy import select, update
from model.job_application_model import JobApplicationModel
from model.job_post_model import JobPostModel
from model.user_model import UserModel
from repository.base_repository import BaseRepository
from schema.job_application_schema import JobApplication, JobApplicationCreate
from schema.job_post_schema import JobPostCreate, JobPostPageRequest, JobPostUpdate
from sqlalchemy.orm import selectinload


class JobRepository(BaseRepository):
    async def get_job_post_page(self, jop_post_page_request: JobPostPageRequest) -> List[JobPostModel]:
        page_size = 10

        stmt = select(JobPostModel).where(JobPostModel.active == True).where(JobPostModel.active)
        if jop_post_page_request.key_word:
            stmt = stmt.where(JobPostModel.title.ilike(f"%{jop_post_page_request.key_word}%"))
        if jop_post_page_request.education_level:
            stmt = stmt.where(JobPostModel.education_level == jop_post_page_request.education_level)
        if jop_post_page_request.employ_type:
            stmt = stmt.where(JobPostModel.employ_type == jop_post_page_request.employ_type)
        if jop_post_page_request.region or jop_post_page_request.region != []:
            stmt = stmt.where(JobPostModel.location.in_(jop_post_page_request.region))
        if jop_post_page_request.salary:
            stmt = stmt.where(JobPostModel.salary >= jop_post_page_request.salary)

        stmt = stmt.offset(jop_post_page_request.page * page_size).limit(page_size)
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res

    async def get_job_post_by_id(self, post_id: str) -> JobPostModel:
        stmt = select(JobPostModel).where(JobPostModel.post_id == post_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res

    async def create_job_post(self, job_post_create: JobPostCreate) -> JobPostModel:
        job_post = JobPostModel(**job_post_create.model_dump())
        self.session.add(job_post)
        await self.session.flush()
        return job_post

    async def update_job_post(self, post_id: str, job_post_create: JobPostUpdate) -> JobPostModel:
        stmt = select(JobPostModel).where(JobPostModel.post_id == post_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        update_data = job_post_create.model_dump(exclude_none=True)  # None이 아닌 값만 추출
        for key, value in update_data.items():
            setattr(res, key, value)

        return res

    async def delete_job_post(self, post_id: str) -> str:
        stmt = select(JobPostModel).where(JobPostModel.post_id == post_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        if res:
            res.active = False
            return post_id
        else:
            return None

    async def bookmark_job_post(self, post_id: str, user_id: UUID) -> List[UUID]:
        stmt = select(UserModel).where(UserModel.id == user_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        if res.bookmark is None:
            res.bookmark = []
        res.bookmark.append(post_id)
        await self.session.flush()

        return res.bookmark

    async def get_bookmark_job_post(self, user_id=UUID) -> List[UUID]:
        stmt = select(UserModel).where(UserModel.id == user_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res.bookmark

    async def get_bookmark_job_post_list(self, bookmark_list: List[UUID]) -> List[JobPostModel]:
        if not bookmark_list:  # 리스트가 비어 있으면 빈 결과 반환
            return []
        stmt = select(JobPostModel).where(JobPostModel.post_id.in_(bookmark_list))
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res

    # ------------------------
    async def job_apply(self, job_appication_create: JobApplicationCreate):

        # TODO

        pass

    async def job_application_cancel(self, user_id: UUID, application_id: str):
        # 실제 지원자가 자신의 계정으로 삭제하는것을 위해 user_id로 필터링
        stmt = (
            update(JobApplicationModel)
            .where(JobApplicationModel.user_id == user_id)
            .where(JobApplicationModel.application_id == application_id)
            .values(activate=False)
            .returning(JobApplicationModel)
        )
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res

    async def get_my_application(self, user_id: UUID) -> List[JobApplicationModel]:
        stmt = select(JobApplicationModel).where(JobApplicationModel.user_id == user_id)
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res
