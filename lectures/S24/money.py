from typing import *


def positive_values(nums: List[float]) -> List[float]:
    result = []
    i = 0
    while i < len(nums):
        if nums[i] > 0:
            result.append(nums[i])
        i += 1
    return result


def purge_negative(nums: List[float]):
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            nums.pop(i)
        else:
            i += 1


def add_percent(nums: List[float], increment: float):
    i = 0
    while i < len(nums):
        nums[i] *= 1 + increment
        i += 1