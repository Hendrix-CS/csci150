from typing import *

def num_upper_case(s: str) -> int:
    count = 0
    for letter in s:
        if letter.isupper():
            count += 1
    return count


def num_double_letters(s: str) -> int:
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count

def ascending_1(nums: List[int]) -> bool:
    last_num = nums[0]
    for n in nums[1:]:
        if last_num > n:
            return False
        last_num = n
    return True

def ascending_2(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def lines_with(filename: str, target: str) -> List[str]:
    with open(filename) as file_handle:
        file_handle = open(filename)
        result = []
        for line in file_handle:
            if target in line:
                result.append(line)
        return result