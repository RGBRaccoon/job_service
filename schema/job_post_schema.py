from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict

from enums.close_type import CloseType
from enums.educatrion_level import EducationLevel
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
    location: Optional[str] = None
    job_type: Optional[str] = None
    job_code: Optional[str] = None
    experience_level: Optional[ExperienceLevel] = None
    salary: Optional[SalaryType] = None
    education_level: Optional[EducationLevel] = None
    read_cnt: int
    apply_cnt: int
    model_config = ConfigDict(from_attributes=True)


class JobPostCreate(JobPost):
    read_cnt: int = 0
    apply_cnt: int = 0
    model_config = ConfigDict(from_attributes=True)


class JobPostUpdate(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    posting_timestamp: Optional[int] = None
    modification_timestamp: Optional[int] = None
    opening_timestamp: Optional[int] = None
    expiration_timestamp: Optional[int] = None
    close_type: Optional[CloseType] = None
    company: Optional[Company] = None
    location: Optional[SecondLocationCode] = None
    job_type: Optional[JobType] = None
    job_code: Optional[int] = None
    experience_level: Optional[ExperienceLevel] = None
    salary: Optional[SalaryType] = None
    experience_min: Optional[int] = None
    experience_max: Optional[int] = None
    education_level: Optional[EducationLevel] = None
    read_cnt: Optional[int] = None
    apply_cnt: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


class JobPostResponse(JobPost):
    model_config = ConfigDict(from_attributes=True)


class JobPostListData(BaseModel):
    post_id: UUID
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
    region: List[SecondLocationCode]
    salary: Optional[SalaryType] = None
