from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

# PostgreSQL 연결 URL 설정
# DATABASE_URL = "postgresql+asyncpg://username:password@localhost:5432/dbname"
DATABASE_URL = env_vars["DATABASE_URL"]
SYNC_DATABASE_URL = env_vars["SYNC_DATABASE_URL"]
# 비동기 SQLAlchemy 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# 비동기 세션 팩토리 생성
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


# Base 클래스 생성
Base = declarative_base()


sync_engine = create_engine(SYNC_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


def create_db():
    # 동기 방식으로 테이블 생성
    Base.metadata.create_all(bind=sync_engine)


async def get_async_session():
    async with async_session() as session:
        yield session
