def same_char(s: str, t: str) -> int:
    count: int = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1

    return count


def sum_between(a: int, b: int) -> int:
    s: int = 0   # current sum
    for n in range(a, b+1):
        s += n
    return s


def sum_between2(a: int, b: int) -> int:
    s: int = 0
    n: int = a
    while n <= b:
        s += n
        n += 1
    return s


def sum_between3(a: int, b: int) -> int:
    if a > b:      # redundant, but fine
        return 0

    s: int = 0
    n: int = a
    while n <= b:
        s += n
        n += 1
    return s


def my_replace(s: str, t: str, u: str) -> str:
    new_s: str = ''
    for c in s:
        if c == t:
            new_s += u
        else:
            new_s += c
    return new_s


from typing import *

def list_min(lst: List[int]) -> int:
    smallest: int = lst[0]
    smallest_index: int = 0
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index