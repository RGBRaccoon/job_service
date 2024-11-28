from pydantic import BaseModel


class JobPost(BaseModel):
    pass


class JobPostCreate(JobPost):
    pass


class JobPostResponse(JobPost):
    pass


class JobPostPageRequest(BaseModel):
    pass
