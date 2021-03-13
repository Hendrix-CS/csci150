from typing import *

# nums: List[int] = [1,2,3]
# nums2 = nums
# nums[1] = 0
# print(nums2)

def release(animals: List[str]):
    while len(animals) > 2:
        animals.pop(0)

def main():
    animals: List[str] = \
        ['hippo', 'tortoise', 'salamander', 'fish', 'frog']

    release(animals)
    print(animals)

main()