from enum import Enum


class FiringResult(Enum):
    MISSED = 0
    HIT = 1
    REPEAT = 2
