from uuid import UUID
from pydantic import BaseModel, ConfigDict


class JobApplication(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pass


class JobApplicationCreate(JobApplication):
    user_id: UUID
    pass


class JobApplicationResponse(JobApplication):
    pass
