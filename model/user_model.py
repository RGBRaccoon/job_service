from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from config.db_config import Base


class UserModel(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"
