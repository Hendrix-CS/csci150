

# nums = [1, 2, 3]
# nums2 = nums
# nums[1] = 0
# print(nums2)

# This is weird!  What's going on!?!?!

# - Variables don't actually store values, they store *references* to objects.
#   A reference "points to" a certain object.
# - Copying one variable into another doesn't actually copy the value,
#   it just copies the reference.
# - Variables which reference things with the same value are equal, which
#   you can test with ==.
# - Variables which reference *the same memory location* are *identical*,
#   which you can test with 'is'.

# lst2 = lst1 does not actually make a copy.
# What if we actually do want a copy?
#
#   lst2 = lst1[:]
#
# Be careful about methods that modify something
# vs. methods that return a new thing.
#
# e.g.
#
#   lst2 = lst1.sort()
#
# would be incorrect because lst1.sort() actually modifies lst1 and does not return anything.
#
# On the other hand,
#
#   str2 = str1.upper()
#
# is correct because str1.upper() returns a new string (strings are immutable).
#
#   str1.upper()
#
# by itself does nothing.

from typing import *
#
# def release(animals: List[str]):
#     while len(animals) > 2:
#         animals.pop(0)
#
# my_animals = ["kookaburra", "quail", "salamander", "razorback"]
#
# release(my_animals)
# print(my_animals)


def slicer(nums: List[int]) -> List[int]:
    first3 = nums[:3]
    first3[2] *= 3
    return first3


def main():
    my_nums = [1, 2, 8, 6, 7, 12]
    n = 3
    my_nums = slicer(my_nums)
    print(my_nums)

main()