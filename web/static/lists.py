from typing import *

# Lists!

# Empty string is ''
# Empty list is []

# Non-empty lists are written
#   [1, 2, 3, 4]

# Stuff that works the same on strings & lists:
#   - len
#   - indexing and slicing
#   -  + operator

# Lists are mutable!
#   e.g.   animals[0] = 'capybara'
#   - append
#   - remove
#   - pop

# Input: a list of ints
# Print each int in the list on a separate line.
# For example, explode_list([2,4,6]) prints
# 2
# 4
# 6
#
# Does not modify the list.
def explode_list(lst):
    n = 0
    while n < len(lst):
        print(lst[n])
        n += 1

def explode_list2(lst):
    x = -len(lst)
    while x != 0:
        print(lst[x])
        x += 1

#######################################

nums = [1,2,3]
nums2 = nums
nums[1] = 77
print(nums2)

# Prints [1,77,3] because nums and nums2 hold *references* to the same list.

def release_animals(animals: List[str]):
    while (len(animals) > 2):
        animals.pop(0)

animals = ['ox', 'fox', 'chicken', 'turkey', 'llama']
release_animals(animals)
print(animals)


#########################################

# For loops

def explode_list_better(lst: List[int]):
    for e in lst:
        print(e)

    # n = 0
    # while n < len(lst):
    #     print(lst[n])
    #     n += 1

def verticalize(s: str):
    for c in s:
        print(c)

# Modifies the list to double every element.
def doubleEvery(lst: List[int]):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2


#############################################
# For loop practice!

# count(s, c) counts how many times character c occurs in string s.
# e.g.  count('hello', 'h') = 1
#       count('hello', 'l') = 2
def count(haystack: str, needle: str) -> int:
    counter = 0
    for c in haystack:
        if c == needle:
            counter += 1
    return counter

# Returns the sum of all the numbers in the list.
# e.g. sum([1,2,3]) = 6
def sum(nums: List[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total

# Return the index of the first occurrence of needle in haystack,
# or -1 if it is not there.
# e.g.
#   find('hello', 'e') = 1
#   find('hello', 'l') = 2
#   find('hello', 'z') = -1
def find(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return -1
