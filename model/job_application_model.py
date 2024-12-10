import uuid
from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from config.db_config import Base


class JobApplicationModel(Base):
    __tablename__ = "job_application"
    application_id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid.uuid4)
    post_id: Mapped[str] = mapped_column(ForeignKey("job_post.post_id", ondelete="CASCADE"))
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    on_process: Mapped[bool] = mapped_column(Boolean)
    write: Mapped[str] = mapped_column(String, nullable=True)
