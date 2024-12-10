from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from enums.close_type import CloseType
from enums.educatrion_level import EducationLevel
from enums.employ_type import EmploymentType
from enums.job_type import JobType
from enums.location_code import SecondLocationCode
from enums.salary_type import SalaryType
from schema.company import Company
from schema.experience_level import ExperienceLevel


class JobPost(BaseModel):
    url: str
    title: str
    posting_timestamp: int
    modification_timestamp: int
    opening_timestamp: int
    expiration_timestamp: int
    close_type: Optional[CloseType] = None
    company: Optional[Company] = None
    location: Optional[SecondLocationCode] = None
    job_type: Optional[JobType] = None
    job_code: int
    experience_level: Optional[ExperienceLevel] = None
    salary: Optional[SalaryType] = None
    experience_min: Optional[int] = None
    experience_max: Optional[int] = None
    education_level: Optional[EducationLevel] = None
    read_cnt: Optional[int] = None
    apply_cnt: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)
    pass


class JobPostCreate(JobPost):
    pass


class JobPostResponse(JobPost):
    pass


class JobPostListData(BaseModel):
    post_id: str
    url: str
    title: str
    expiration_timestamp: int
    company: Optional[Company] = None
    location: Optional[SecondLocationCode] = None
    experience_level: Optional[ExperienceLevel] = None


class JobPostListResponse(BaseModel):
    cur_page: int
    post_list: List[JobPostListData]


class JobPostPageRequest(BaseModel):
    key_word: Optional[str] = None
    page: int = 0
    education_level: Optional[EducationLevel] = None
    empoly_type: Optional[EmploymentType] = None
    region: List[SecondLocationCode]
    salary: Optional[SalaryType] = None
