from typing import Optional
from pydantic import BaseModel


class ExperienceLevel(BaseModel):
    code: int
    min: Optional[int] = None
    max: Optional[int] = None
