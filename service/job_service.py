from typing import List
from repository.job_repository import JobRepository
from schema.job_application_schema import JobApplication, JobApplicationCreate
from schema.job_post_schema import JobPost, JobPostCreate, JobPostListData, JobPostListResponse, JobPostPageRequest, JobPostUpdate
from service.base_service import BaseService
from uuid import UUID


class JobService(BaseService):

    async def get_job_post_page(self, jop_post_page_request: JobPostPageRequest) -> JobPostListResponse:
        res = await JobRepository(session=self.session).get_job_post_page(jop_post_page_request)

        post_list = [
            JobPostListData(
                post_id=i.post_id,
                url=i.url,
                title=i.title,
                expiration_timestamp=i.expiration_timestamp,
                company=i.company,
                location=i.location,
                experience_level=i.experience_level,
            )
            for i in res
        ]
        list_res = JobPostListResponse(cur_page=jop_post_page_request.page, post_list=post_list)

        return list_res

    async def get_job_post_by_id(self, post_id: str) -> JobPost:
        res = await JobRepository(session=self.session).get_job_post_by_id(post_id=post_id)
        return JobPost.model_validate(res)

    async def create_job_post(self, job_post_create: JobPostCreate) -> JobPost:
        res = await JobRepository(session=self.session).create_job_post(job_post_create=job_post_create)
        return JobPost.model_validate(res)

    async def update_job_post(self, post_id: str, job_post_create: JobPostUpdate) -> JobPost:
        res = await JobRepository(session=self.session).update_job_post(post_id=post_id, job_post_create=job_post_create)
        return JobPost.model_validate(res)

    async def delete_job_post(self, post_id: str) -> str:
        res = await JobRepository(session=self.session).delete_job_post(post_id=post_id)
        return res

    async def bookmark_job_post(self, post_id: UUID, user_id: UUID) -> List[UUID]:
        job_repository = JobRepository(session=self.session)
        res = await job_repository.bookmark_job_post(post_id=post_id, user_id=user_id)
        return res

    async def get_bookmark_job_post(self, user_id=UUID) -> List[JobPost]:
        bookmark_list = await JobRepository(session=self.session).get_bookmark_job_post(user_id=user_id)
        res = await JobRepository(session=self.session).get_bookmark_job_post_list(bookmark_list=bookmark_list)
        return [JobPost.model_validate(i) for i in res]

    # ----------------------------------------------------------------------------

    async def job_apply(self, job_appication_create: JobApplicationCreate):
        res = await JobRepository(session=self.session).job_apply(job_appication_create=job_appication_create)
        return res

    async def job_application_cancel(self, user_id: UUID, application_id: str):
        res = await JobRepository(session=self.session).job_application_cancel(user_id=user_id, application_id=application_id)
        return res

    async def get_my_application(self, user_id: UUID) -> List[JobApplication]:
        res = await JobRepository(session=self.session).get_my_application(user_id=user_id)
        return [JobApplication.model_validate(i) for i in res]
