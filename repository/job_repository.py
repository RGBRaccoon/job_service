from typing import List
from uuid import UUID

from sqlalchemy import select, update
from model.job_application_model import JobApplicationModel
from model.job_post_model import JobPostModel
from model.user_model import UserModel
from repository.base_repository import BaseRepository
from schema.job_application_schema import JobApplication, JobApplicationCreate
from schema.job_post_schema import JobPostCreate, JobPostPageRequest
from sqlalchemy.orm import selectinload


class JobRepository(BaseRepository):
    async def get_job_post_page(self, jop_post_page_request: JobPostPageRequest) -> List[JobPostModel]:
        stmt = select(JobPostModel).where(JobPostModel.active == True).where(JobPostModel)
        # TODO

        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res

    async def get_job_post_by_id(self, post_id: str) -> JobPostModel:
        stmt = select(JobPostModel).where(JobPostModel.post_id == post_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res

    async def create_job_post(self, job_post_create: JobPostCreate) -> JobPostModel:
        job_post = JobPostModel(job_post_create.model_dump())
        await self.session.add(job_post)
        await self.session.flush()
        return job_post

    async def update_job_post(self, post_id: str, job_post_create: JobPostCreate):
        # TODO: job_post_create 중에 값이 있는 애만 찾아서 남기고 나머지는 삭제-> 삭제된 칼럼들은 업데이트가
        # 되지 않도록 할 것
        pass

    async def delete_job_post(self, post_id: str) -> str:
        stmt = update(JobPostModel).where(JobPostModel.post_id == post_id).values(activate=False).returning(JobPostModel)
        res = await self.session.execute(stmt)
        if res:
            return post_id

    async def bookmark_job_post(self, bookmark_post: JobPostModel, user_id: UUID):
        stmt = select(UserModel).where(UserModel.id == user_id)
        res = await self.session.execute(stmt)
        res = res.scalar()
        res.bookmark.append(bookmark_post)

        return bookmark_post

    async def get_bookmark_job_post(self, user_id=UUID) -> List[JobPostModel]:
        stmt = select(UserModel).where(UserModel.id == user_id).options(selectinload(UserModel.bookmark))
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res.bookmark

    # ------------------------
    async def job_apply(self, job_appication_create: JobApplicationCreate):
        # TODO

        pass

    async def job_application_cancel(self, application_id: str):
        stmt = (
            update(JobApplicationModel)
            .where(JobApplicationModel.application_id == application_id)
            .values(activate=False)
            .returning(JobApplicationModel)
        )
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res

    async def get_my_application(self, user_id: UUID) -> List[JobApplication]:
        stmt = select(UserModel).where(UserModel.id == user_id).join(UserModel.job_applicaion)
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res
