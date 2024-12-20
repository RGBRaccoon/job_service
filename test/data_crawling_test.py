import asyncio
import csv
import json
import uuid
import requests
import time
from sqlalchemy import inspect
from sqlalchemy import select
from config.db_config import async_session

from enums.close_type import CloseType
from enums.educatrion_level import EducationLevel
from enums.job_type import JobType
from enums.salary_type import SalaryType
from model.job_post_model import JobPostModel
from schema.company import Company
from schema.experience_level import ExperienceLevel
from schema.job_post_schema import JobPostCreate
from service.job_service import JobService


# 데이터 수집부
# 데이터 수집은 인터넷 크롤링 대신 api키를 이용하여 서버에 요청하는 방식으로 이루어짐.
def create_job_post(data: dict) -> JobPostCreate:
    print(data)
    job_post = JobPostCreate(
        url=data["url"],
        title=data["position"]["title"],
        posting_timestamp=data["posting-timestamp"],
        modification_timestamp=data["modification-timestamp"],
        opening_timestamp=data["opening-timestamp"],
        expiration_timestamp=data["expiration-timestamp"],
        close_type=data["close-type"]["code"],
        company=Company(name=data["company"]["detail"]["name"], href=data["company"]["detail"]["href"]),
        location=data["position"]["location"]["code"],
        job_type=data["position"]["job-type"]["code"],
        job_code=data["position"]["job-code"]["code"],
        experience_level=ExperienceLevel(
            code=data["position"]["experience-level"]["code"],
            min=data["position"]["experience-level"]["min"],
            max=data["position"]["experience-level"]["max"],
        ),
        salary=data["salary"]["code"],
        education_level=data["position"]["required-education-level"]["code"],
    )

    return job_post

def transform_value(column_type, value):
    """
    데이터 타입에 맞게 값을 변환합니다.
    """
    if value is None or value == "":
        return None

    try:
        if column_type == uuid.UUID:
            return uuid.UUID(value)
        elif column_type == int:
            return int(value)
        elif column_type == bool:
            return str(value).strip().lower() in ("true", "1", "yes")
        elif column_type == CloseType:
            return CloseType(int(value))
        elif column_type == EducationLevel:
            return EducationLevel(int(value))
        elif column_type == JobType:
            return JobType(int(value))
        elif column_type == SalaryType:
            return SalaryType(int(value))
        elif column_type == dict:
            return eval(value)  # JSON 데이터를 dict로 변환
        elif column_type == str:
            return str(value)
        else:
            return value
    except (ValueError, TypeError):
        return None

async def main():
    access_key = "Access key"  # 발급받은 accessKey 키유출을 막기위해 커밋에는 제외외
    max_retries = 1  # 최대 재시도 횟수
    retry_count = 0

    while retry_count < max_retries:
        try:
            # 검색 키워드 URL 인코딩
            api_url = f"https://oapi.saramin.co.kr/job-search?access-key={access_key}&job_type=&edu_lv=&count=150"

            # GET 요청
            headers = {"Accept": "application/json"}
            response = requests.get(api_url, headers=headers)

            # 응답 처리
            if response.status_code == 200:
                # 정상 호출
                # print(response.json())
                data_parts = []  # 데이터를 저장할 임시 리스트

                for i in response:
                    data_parts.append(i)  # 데이터를 리스트에 추가

                # 리스트의 모든 bytes를 결합
                data = b"".join(data_parts)

                json_data = json.loads(data.decode("utf-8"))

                job_list = [create_job_post(i) for i in json_data["jobs"]["job"]]

                async with async_session() as session:
                    for i in job_list:
                        await JobService(session=session).create_job_post(job_post_create=i)
                    await session.commit()
                break
            else:
                # 에러 발생
                print(f"Error: {response.status_code}", response.text)
                retry_count += 1
                time.sleep(2)  # 재시도 전 대기 시간

        except Exception as e:
            print(f"Exception occurred: {e}")
            retry_count += 1
            time.sleep(2)  # 재시도 전 대기 시간

        if retry_count == max_retries:
            print("Max retries reached. Request failed.")


async def export_data():
    async with async_session() as session:
        stmt = select(JobPostModel)
        results = await session.execute(stmt)
        results = results.scalars().all()

        with open("job_post.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            # 헤더 작성
            writer.writerow([column.name for column in JobPostModel.__table__.columns])
            # 데이터 작성
            for row in results:
                writer.writerow([getattr(row, column.name) for column in JobPostModel.__table__.columns])

async def import_data():
    with open("job_post.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)  # CSV 헤더를 기반으로 딕셔너리로 읽음

        # SQLAlchemy 모델의 메타데이터를 기반으로 컬럼 타입 매핑
        mapper = inspect(JobPostModel)
        column_types = {column.name: column.type.python_type for column in mapper.columns}

        data_list = []
        for row in reader:
            transformed_row = {}

            for column, value in row.items():
                if column in column_types:
                    transformed_row[column] = transform_value(column_types[column], value)

            # JobPostModel 객체 생성
            data_list.append(JobPostModel(**transformed_row))

    # 데이터베이스에 삽입
    async with async_session() as session:
        session.add_all(data_list)
        await session.commit()


asyncio.run(import_data())
