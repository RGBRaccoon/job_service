from typing import List
from repository.job_repository import JobRepository
from schema.job_application_schema import JobApplication, JobApplicationCreate
from schema.job_post_schema import JobPostCreate, JobPostPageRequest
from service.base_service import BaseService
from uuid import UUID


class JobService(BaseService):

    async def get_job_post_page(self, jop_post_page_request: JobPostPageRequest):
        res = await JobRepository(session=self.session).get_job_post_page(jop_post_page_request)
        # 리스트로 반환해야됨.

    async def create_job_post(self, job_post_create: JobPostCreate):
        res = await JobRepository(session=self.session).create_job_post(job_post_create=job_post_create)
        return res

    async def update_job_post(self, job_post_create: JobPostCreate):
        res = await JobRepository(session=self.session).update_job_post(job_post_create=job_post_create)
        return res

    async def delete_job_post(self, post_id: str):
        res = await JobRepository(session=self.session).delete_job_post(post_id=post_id)
        return res

    async def job_apply(self, job_appication_create: JobApplicationCreate):
        res = await JobRepository(session=self.session).job_apply(job_appication_create=job_appication_create)
        return res

    async def job_application_cancel(self, application_id: str):
        res = await JobRepository(session=self.session).job_application_cancel(application_id=application_id)
        return res

    async def get_my_application(self, user_id: UUID) -> List[JobApplication]:
        res = await JobRepository(session=self.session).get_my_application(user_id=user_id)
        return res
