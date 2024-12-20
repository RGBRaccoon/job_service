import uuid
from sqlalchemy import String, Boolean, JSON, Integer, UUID
from config.db_config import Base
from enums.close_type import CloseType
from enums.educatrion_level import EducationLevel
from enums.job_type import JobType
from enums.salary_type import SalaryType
from model.job_application_model import JobApplicationModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from schema.company import Company
from schema.experience_level import ExperienceLevel


class JobPostModel(Base):
    __tablename__ = "job_post"
    post_id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    url: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    posting_timestamp: Mapped[int] = mapped_column(Integer)
    modification_timestamp: Mapped[int] = mapped_column(Integer)
    opening_timestamp: Mapped[int] = mapped_column(Integer)
    expiration_timestamp: Mapped[int] = mapped_column(Integer)
    close_type: Mapped[CloseType] = mapped_column(Integer)
    company: Mapped[Company] = mapped_column(JSON)
    location: Mapped[str] = mapped_column(String)
    job_type: Mapped[str] = mapped_column(String)
    job_code: Mapped[str] = mapped_column(String)
    experience_level: Mapped[ExperienceLevel] = mapped_column(JSON)
    salary: Mapped[SalaryType] = mapped_column(Integer)
    experience_min: Mapped[int] = mapped_column(Integer, nullable=True)
    experience_max: Mapped[int] = mapped_column(Integer, nullable=True)
    education_level: Mapped[EducationLevel] = mapped_column(Integer, nullable=True)
    read_cnt: Mapped[int] = mapped_column(Integer, nullable=True)
    apply_cnt: Mapped[int] = mapped_column(Integer, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    job_applicaion: Mapped[JobApplicationModel] = relationship("JobApplicationModel")
