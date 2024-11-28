from typing import List
from schema.job_application_schema import JobApplication, JobApplicationCreate
from schema.job_post_schema import JobPostCreate, JobPostPageRequest
from service.base_service import BaseService
from uuid import UUID


class JobService(BaseService):

    async def get_job_post_page(jop_post_page_request: JobPostPageRequest):
        pass

    async def create_job_post(job_post_create: JobPostCreate):
        pass

    async def update_job_post(job_post_create: JobPostCreate):
        pass

    async def delete_job_post(post_id: str):
        pass

    async def job_apply(job_appication_create: JobApplicationCreate):
        pass

    async def job_application_cancel(application_id: str):
        pass

    async def get_my_application(user_id: UUID) -> List[JobApplication]:
        pass
