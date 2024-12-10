from enum import IntEnum


class JobType(IntEnum):
    FULL_TIME = 1  # 정규직
    CONTRACT = 2  # 계약직
    MILITARY_SPECIAL = 3  # 병역특례
    INTERN = 4  # 인턴직
    PART_TIME = 5  # 아르바이트
    DISPATCH = 6  # 파견직
    OVERSEAS_EMPLOYMENT = 7  # 해외취업
    COMMISSION = 8  # 위촉직
    FREELANCER = 9  # 프리랜서
    CONTRACT_WITH_PERM = 10  # 계약직 (정규직 전환가능)
    INTERN_WITH_PERM = 11  # 인턴직 (정규직 전환가능)
    TRAINEE = 12  # 교육생
    SPECIAL_APPOINTMENT = 13  # 별정직
    PART = 14  # 파트
    FULL_TIME_RESEARCHER = 15  # 전임
    FIXED_TERM = 16  # 기간제
    PERMANENT_CONTRACT = 17  # 무기계약직
    PROFESSIONAL_CONTRACT = 18  # 전문계약직
    PROFESSIONAL_RESEARCH = 19  # 전문연구요원
    INDUSTRIAL_FUNCTIONAL = 20  # 산업기능요원
    ACTIVE_SERVICE = 21  # 현역
    RESERVIST = 22  # 보충역
