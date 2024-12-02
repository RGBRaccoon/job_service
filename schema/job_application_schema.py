from pydantic import BaseModel, ConfigDict


class JobApplication(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pass


class JobApplicationCreate(JobApplication):
    pass


class JobApplicationResponse(JobApplication):
    pass
