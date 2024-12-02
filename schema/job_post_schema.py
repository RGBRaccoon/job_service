from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from enums.educatrion_level import EducationLevel
from enums.employ_type import EmploymentType
from enums.location_code import SecondLocationCode
from enums.salary_type import SalaryType


class JobPost(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pass


class JobPostCreate(JobPost):
    pass


class JobPostResponse(JobPost):
    pass


class JobPostPageRequest(BaseModel):
    key_word: Optional[str] = None
    page: int = 0
    education_level: Optional[EducationLevel] = None
    empoly_type: Optional[EmploymentType] = None
    region: List[SecondLocationCode]
    salary: Optional[SalaryType] = None
