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

# Return the index of the first occurrence of the character
# 'needle' in the string 'haystack', or -1 if it is not
# found.
#
#   e.g. find('banana', 'a') = 1
#        find('banana', 'n') = 2
#        find('banana', 'z') = -1
# def find(haystack: str, needle: str) -> int:
#     for c in haystack:
#         if c == needle:
#             # We're stuck!  We need to return the *index*
#             # of c, but we don't have that information.
#             return ???
#
#     # Didn't find it
#     return -1

# Reasons we might want to use  for i in range(...):
#   1. We want to use or return the index
#   2. We want to modify the elements of the list
#   3. We want to look at more than one element of the list
#      at a time.

def find(haystack: str, needle: str) -> int:
    # conceptually we want this:
    # for i in [0, 1, 2, 3, ..., len(haystack) - 1]:

    # the range function can make lists like this for us.
    # This will loop over the list of all valid indices
    # for the string haystack.
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i

    return -1

animals: List[str] = ['capybara', 'squid', 'orca', 'lemur']

for animal in animals:
    animal += '!'

# >>> animals
# ['capybara', 'squid', 'orca', 'lemur']
# >>> x = animals[2]
# >>> x
# 'orca'
# >>> x += '!'
# >>> x
# 'orca!'
# >>> animals
# ['capybara', 'squid', 'orca', 'lemur']
# >>> animals[2] += '!'
# >>> animals
# ['capybara', 'squid', 'orca!', 'lemur']

# If we actually want to change the entries in animals:

for i in range(len(animals)):
    animals[i] += '!'

# Return whether the list is in order from smallest
# to biggest.
#
#   e.g. is_sorted([2,5,6,9,9]) = True
#        is_sorted([2,5,3,9,9]) = False
#        is_sorted([]) = True
def is_sorted(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False
    return True