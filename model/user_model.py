from typing import List
import uuid
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from config.db_config import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import UUID
from model.job_application_model import JobApplicationModel
from sqlalchemy.dialects.postgresql import ARRAY


class UserModel(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    job_applicaion: Mapped[JobApplicationModel] = relationship("JobApplicationModel")
    bookmark: Mapped[List[uuid.UUID]] = mapped_column(ARRAY(UUID), nullable=False)
