def all_suffixes(s: str):
    i = 0
    while i < len(s):
        print(s[i:])
        i += 1


def into_middle(s: str):
    start = 0
    end = len(s)
    while start < end:
        print(f"[{s[start:end]}]")
        start += 1
        end -= 1


def is_present(looking_for: str, target: str) -> bool:
    i = 0
    while i < len(target):
        if target[i:i + len(looking_for)] == looking_for:
            return True
        i += 1
    return False


from typing import List
def add_them_up(nums: List[int]) -> int:
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total


def odds(n: int) -> List[int]:
    result = []
    while len(result) < n:
        if len(result) == 0:
            result.append(1)
        else:
            result.append(result[-1] + 2)
    return result