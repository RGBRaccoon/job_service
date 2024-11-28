import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from config.db_config import Base


class JobPostModel(Base):
    __tablename__ = "job_post"
    post_id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
