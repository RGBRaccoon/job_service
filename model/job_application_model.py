import uuid
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from config.db_config import Base


class JobApplicationModel(Base):
    __tablename__ = "job_application"
    application_id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid.uuid4)
    post_id: Mapped[str] = mapped_column(ForeignKey("job_post.post_id", ondelete="CASCADE"))
