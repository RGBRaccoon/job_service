from asyncio import sleep
import os
from unittest import TestCase
import chromedriver_autoinstaller
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL = "https://www.saramin.co.kr/zf_user/jobs/list/domestic"


# chrome_options = Options()
# chrome_options.add_argument("--headless")  # GUI 없이 실행 (선택)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Chromedriver 서비스 생성
# service = Service()
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # 테스트: Google 열기
# driver.get("https://www.google.com")
# print(driver.title)

# # 드라이버 종료
# driver.quit()


def test_crawling():
    # Multi Process PID
    url = "https://www.saramin.co.kr/zf_user/jobs/list/domestic?page=1&page_count=100"
    headers = {"User-Agent": "Mozilla/5.0"}  # 브라우저처럼 보이기 위한 헤더
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    # Step 2: BeautifulSoup로 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    # Step 3: 채용 객체 리스트 추출
    content = soup.find("ul", {"class": "list_product list_grand"})
    job_list = []
    print(content)
    job_items = content.find_all("li", {"class": "item"})
    job_list.extend(job_items)  # 각 채용 객체를 리스트에 추가
    # 결과 확인
    print(f"채용 객체 수: {len(job_list)}")


test_crawling()

# soup = BeautifulSoup(html, "html.parser")
# link = soup.find("a")["href"] if soup.find("a") else "링크 없음"

# # 이미지 URL
# logo = soup.find("img")["src"] if soup.find("img") else "이미지 없음"

# # 제목
# title = soup.find("strong", {"class": "tit"}).get_text(strip=True) if soup.find("strong", {"class": "tit"}) else "제목 없음"

# # 회사명
# company = soup.find("span", {"class": "corp"}).get_text(strip=True) if soup.find("span", {"class": "corp"}) else "회사 없음"

# # 지역
# location = (
#     soup.find("li", {"class": "company_local ellipsis"}).get_text(strip=True)
#     if soup.find("li", {"class": "company_local ellipsis"})
#     else "지역 없음"
# )

# # 경력
# experience = soup.find_all("li")[1].get_text(strip=True) if len(soup.find_all("li")) > 1 else "경력 없음"

# # 학력
# education = soup.find_all("li")[2].get_text(strip=True) if len(soup.find_all("li")) > 2 else "학력 없음"

# # 마감일
# deadline = soup.find("span", {"class": "date"}).get_text(strip=True) if soup.find("span", {"class": "date"}) else "마감일 없음"
