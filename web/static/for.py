# For loops

# Common pattern:

animals = ["chicken", "rat", "stingray", "cow"]

# i: int = 0
# while i < len(animals):
#     print(animals[i])
#     i += 1

# Above works, but it's annoying because:
#   - Have to make variable i
#   - Have to get the test (< len) right
#   - Have to remember to update i
#   - etc.

# Better way:

for a in animals:
    print(a)

# In general:

# for <new variable> in <list expression>:
#    ... do stuff with variable ...

# Also works for strings:

# for c in "hello":
#     print(c)
#
# for c in "hello":
#     print(c)
#     if c < 'i':
#         print("!!!")

print(animals)

for a in animals:
    a = a + "!"

# print(a)
print(animals)

for a in '':     # Does nothing!
    print(10/0)

# Count how many times c occurs in s
# e.g. count('banana', 'n') = 2
def count(s: str, c: str) -> int:

    num_occurrences: int = 0
    for a in s:
        if a == c:
            num_occurrences += 1

    return num_occurrences

from typing import *

# Return a list containing only the elements with len >= 5
# e.g. filter_long(["hi", "there", "xy", "abcdefgh"]) = ["there", "abcdefgh"]
def filter_long(things: List[str]) -> List[str]:
    new_list: List[str] = []
    for thing in things:
        if len(thing) >= 5:
            new_list.append(thing)
    return new_list

# Want a way to use a for loop but get access to the indices.

for i in range(len(animals)):
    animals[i] += '!'

print(animals)

# Reasons for looping over indices instead of looping over elements directly:
#
# - To be able to modify the list as we go
# - To be able to use or remember the indices for later
# - To loop over two lists at the same time
# - To compare items that are next to each other

# Return the index of the first occurrence of the target character in s,
# or -1 if it is not found.

# First attempt, doesn't work:
# def find(s: str, target: str):
#     for c in s:
#         if c == target:
#             return ????  # We have no index to return here!

def find(s: str, target: str):
    for i in range(len(s)):
        if s[i] == target:
            return i

    return -1

# Return a list of all the indices where target occurs in s.
# e.g. find_all('banana', 'a') = [1,3,5]
#      find_all('banana', 'z') = []
def find_all(s: str, target: str):
    indices: List[int] = []
    for q in range(len(s)):
        if s[q] == target:
            indices.append(q)
    return indices

# Return true if the list is sorted from smallest to biggest.
# e.g.  is_sorted([1,2,3,3,5,99]) = True
#       is_sorted([1,2,3,3,5,4,99]) = False
#       is_sorted([]) =
def is_sorted(nums: List[int]) -> bool:
    for i in range(len(nums)):
        if i+1 < len(nums):
            if nums[i] > nums[i+1]:
                return False
    return True

def is_sorted2(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False
    return True

def is_sorted3(nums: List[int]) -> bool:
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True