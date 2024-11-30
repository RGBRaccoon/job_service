from typing import List
from uuid import UUID

from sqlalchemy import select, update
from model.job_application_model import JobApplicationModel
from model.job_post_model import JobPostModel
from model.user_model import UserModel
from repository.base_repository import BaseRepository
from schema.job_application_schema import JobApplication, JobApplicationCreate
from schema.job_post_schema import JobPostCreate, JobPostPageRequest


class JobRepository(BaseRepository):
    async def get_job_post_page(self, jop_post_page_request: JobPostPageRequest):
        stmt = select(JobPostModel)

        res = await self.session.execute(stmt)
        res = res.scalars().all()

    async def create_job_post(self, job_post_create: JobPostCreate):
        job_post = JobPostModel()

        await self.session.add(job_post)
        return job_post

    async def update_job_post(self, job_post_create: JobPostCreate):
        pass

    async def delete_job_post(self, post_id: str):
        pass

    # ------------------------
    async def job_apply(self, job_appication_create: JobApplicationCreate):
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
