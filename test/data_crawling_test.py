import json
import requests
from urllib.parse import quote
import time

from model.job_post_model import JobPostModel
from schema.company import Company
from schema.experience_level import ExperienceLevel
from schema.job_post_schema import JobPost, JobPostCreate


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


def main():
    access_key = "Pc6PML7bb5VNNXv1k52ucuJ0cEHYU8vjds60fLOmobmsex7MTX3Oi"  # 발급받은 accessKey
    max_retries = 1  # 최대 재시도 횟수
    retry_count = 0

    while retry_count < max_retries:
        try:
            # 검색 키워드 URL 인코딩
            text = quote("")
            api_url = f"https://oapi.saramin.co.kr/job-search?access-key=Pc6PML7bb5VNNXv1k52ucuJ0cEHYU8vjds60fLOmobmsex7MTX3Oi&job_type=&edu_lv=&count=1"

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
                # print(type(json_data))
                # print(json_data)
                # print(json_data["jobs"]["job"][0]["url"])
                job_list = []
                for i in json_data["jobs"]["job"]:
                    job_post = create_job_post(i)
                    job_list.append(job_post)

                # job_post = JobPost.model_validate(json_data)
                # print(job_post)
                # data = JobPostModel(job_post)
                # print(data)
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


if __name__ == "__main__":
    main()
