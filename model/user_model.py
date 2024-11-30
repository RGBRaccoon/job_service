from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from config.db_config import Base
from sqlalchemy.orm import Mapped, relationship

from model.job_application_model import JobApplicationModel


class UserModel(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    job_applicaion: Mapped[JobApplicationModel] = relationship("JobApplicationModel")
