import uuid
from sqlalchemy import String
from config.db_config import Base
from model.job_application_model import JobApplicationModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class JobPostModel(Base):
    __tablename__ = "job_post"
    post_id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)

    job_applicaion: Mapped[JobApplicationModel] = relationship("JobApplicationModel")
