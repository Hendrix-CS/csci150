# For loops

from typing import *

# Previously we wrote code like this to look at each item
# of a list:
def prod_list(nums: List[int]) -> int:
    i: int = 0
    prod_so_far: int = 1
    while i < len(nums):
        prod_so_far *= nums[i]
        i += 1
    return prod_so_far

# This is so common that Python gives us a nicer way to do it:
def prod_list2(nums: List[int]) -> int:
    prod_so_far: int = 1
    for n in nums:
        print(n)
        prod_so_far *= n
    return prod_so_far

# General syntax of a for loop:
# for <new variable> in <list or string>:
#   do stuff (potentially) using the variable

# The stuff will get repeated once for each
# item in the list or character in the string.
# The variable will be assigned each item or character
# in turn.

# Examples

# Count the number of times the character 'needle'
# occurs in the string 'haystack'.  For example,
#   count('banana', 'n') = 2
#   count('banana', 'z') = 0
def count(haystack: str, needle: str) -> int:
    num_needles: int = 0
    for c in haystack:
        if c == needle:
            num_needles += 1
    return num_needles

# Return a new list with only the strings of length 5 or more.
# e.g.
#   filter_long(['hi', 'there', '150', 'abcdefgh'])
#     = ['there', 'abcdefgh']
def filter_long(strs: List[str]) -> List[str]:
    result: List[str] = []
    for s in strs:
        if len(s) >= 5:
            result.append(s)

    return result


# Say whether haystack contains the needle
#   e.g.  contains([1,2,3,4], 3) = True
#         contains([1,2,3,4], 7) = False
def contains(haystack: List[int], needle: int) -> bool:
    found: bool = False   # haven't found the needle yet
    for n in haystack:
        if n == needle:
            found = True
    return found

def contains2(haystack: List[int], needle: int) -> bool:
    for n in haystack:
        if n == needle:
            return True

    return False


def contains3(haystack: List[int], needle: int) -> bool:
    found: bool = False
    for n in haystack:
        found = found or (n == needle)

    return found
