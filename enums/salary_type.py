from enum import IntEnum


class SalaryType(IntEnum):
    COMPANY_POLICY = 0  # 회사내규에 따름
    ABOVE_2600K = 9  # 2,600만원 이상
    ABOVE_2800K = 10  # 2,800만원 이상
    ABOVE_3000K = 11  # 3,000만원 이상
    ABOVE_3200K = 12  # 3,200만원 이상
    ABOVE_3400K = 13  # 3,400만원 이상
    ABOVE_3600K = 14  # 3,600만원 이상
    ABOVE_3800K = 15  # 3,800만원 이상
    ABOVE_4000K = 16  # 4,000만원 이상
    ABOVE_5000K = 17  # 5,000만원 이상
    ABOVE_6000K = 18  # 6,000만원 이상
    ABOVE_7000K = 19  # 7,000만원 이상
    RANGE_8000_TO_9000K = 20  # 8,000~9,000만원
    RANGE_9000_TO_10000K = 21  # 9,000~1억원
    ABOVE_10000K = 22  # 1억원 이상
    NEGOTIABLE_AFTER_INTERVIEW = 99  # 면접후 결정
    MONTHLY = 101  # 월급
    WEEKLY = 102  # 주급
    DAILY = 103  # 일급
    HOURLY = 104  # 시급
    PER_TASK = 105  # 건당
