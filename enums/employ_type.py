from enum import IntEnum


class EmploymentType(IntEnum):
    REGULAR = 1  # 정규직
    CONTRACT = 2  # 계약직
    MILITARY_SPECIAL = 3  # 병역특례
    INTERN = 4  # 인턴직
    PART_TIME = 5  # 아르바이트
    DISPATCH = 6  # 파견직
    OVERSEAS = 7  # 해외취업
    COMMISSION = 8  # 위촉직
    FREELANCE = 9  # 프리랜서
    CONTRACT_TO_REGULAR = 10  # 계약직 (정규직 전환가능)
    INTERN_TO_REGULAR = 11  # 인턴직 (정규직 전환가능)
    TRAINEE = 12  # 교육생
    SPECIAL = 13  # 별정직
    PART = 14  # 파트
    FULL_TIME = 15  # 전임
    LIMITED_TERM = 16  # 기간제
    PERMANENT = 17  # 무기계약직
    PROFESSIONAL_CONTRACT = 18  # 전문계약직
    PROFESSIONAL_RESEARCHER = 19  # 전문연구요원
    INDUSTRIAL_ENGINEER = 20  # 산업기능요원
    ACTIVE_DUTY = 21  # 현역
    RESERVE = 22  # 보충역
