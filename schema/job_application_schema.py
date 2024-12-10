from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class JobApplication(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class JobApplicationCreate(JobApplication):
    user_id: Optional[UUID] = None


class JobApplicationResponse(JobApplication):
    pass
