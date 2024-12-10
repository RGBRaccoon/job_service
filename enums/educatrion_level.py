from enum import IntEnum


class EducationLevel(IntEnum):
    NO_REQUIREMENT = 0  # 학력무관
    HIGH_SCHOOL = 1  # 고등학교졸업
    COLLEGE_2_3_YEAR = 2  # 대학졸업(2,3년)
    UNIVERSITY_4_YEAR = 3  # 대학교졸업(4년)
    MASTER = 4  # 석사졸업
    DOCTOR = 5  # 박사졸업
    HIGH_SCHOOL_OR_HIGHER = 6  # 고등학교졸업이상
    COLLEGE_2_3_YEAR_OR_HIGHER = 7  # 대학졸업(2,3년)이상
    UNIVERSITY_4_YEAR_OR_HIGHER = 8  # 대학교졸업(4년)이상
    MASTER_OR_HIGHER = 9  # 석사졸업이상
