from enum import Enum


class CloseType(Enum):
    APPLICATION_DEADLINE = 1  # 접수 마감일
    UNTIL_HIRED = 2  # 채용시
    ALWAYS_OPEN = 3  # 상시
    OCCASIONAL = 4  # 수시
