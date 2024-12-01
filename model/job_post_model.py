from datetime import datetime
import uuid
from sqlalchemy import String, Boolean, JSON, Integer
from config.db_config import Base
from enums.close_type import CloseType
from enums.educatrion_level import EducationLevel
from enums.job_type import JobType
from enums.location_code import SecondLocationCode
from enums.salary_type import SalaryType
from model.job_application_model import JobApplicationModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from schema.company import Company
from schema.experience_level import ExperienceLevel


class JobPostModel(Base):
    __tablename__ = "job_post"
    post_id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid.uuid4)
    url: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    posting_timestamp: Mapped[int] = mapped_column(Integer)
    modification_timestamp: Mapped[int] = mapped_column(Integer)
    opening_timestamp: Mapped[int] = mapped_column(Integer)
    expiration_timestamp: Mapped[int] = mapped_column(Integer)
    close_type: Mapped[CloseType] = mapped_column(Integer)
    company: Mapped[Company] = mapped_column(JSON)
    location: Mapped[SecondLocationCode] = mapped_column(Integer)
    job_type: Mapped[JobType] = mapped_column(Integer)
    job_code: Mapped[int] = mapped_column(Integer)
    experience_level: Mapped[ExperienceLevel] = mapped_column(JSON)
    salary: Mapped[SalaryType] = mapped_column(Integer)
    experience_min: Mapped[int] = mapped_column(Integer, nullable=True)
    experience_max: Mapped[int] = mapped_column(Integer, nullable=True)
    education_level: Mapped[EducationLevel] = mapped_column(String, nullable=True)
    read_cnt: Mapped[int] = mapped_column(Integer, nullable=True)
    apply_cnt: Mapped[int] = mapped_column(Integer, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean)

    job_applicaion: Mapped[JobApplicationModel] = relationship("JobApplicationModel")
