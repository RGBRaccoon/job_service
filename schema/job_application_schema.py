from pydantic import BaseModel


class JobApplication(BaseModel):
    pass


class JobApplicationCreate(JobApplication):
    pass


class JobApplicationResponse(JobApplication):
    pass
