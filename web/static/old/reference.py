

# nums = [1,2,3]
# nums2 = nums
# nums[1] = 0
# print(nums2)
#

from typing import *

# def release(animals: List[str]):
#     while len(animals) > 2:
#         animals.pop()
#
# my_animals = ['dog', 'cat', 'mouse', 'rabbit', 'shark1', 'shark2', 'shark3', 'potato']
# release(my_animals)
# print(my_animals)
#
#

def slicer(nums: List[int]) -> List[int]:
    first3 = nums[:3]
    first3[2] *= 3
    return first3

def main():
    my_nums = [1,2,8,6,7,12]
    my_nums = slicer(my_nums)
    print(my_nums)

main()

