from typing import *

# Recall n! (n factorial) = 1 * 2 * 3 * ... * n

def factorial_while(n: int) -> int:
    factorial_n = 1
    count = 1
    while count <= n:
        factorial_n *= count
        count += 1
    return factorial_n

# With a for loop?
def factorial_for(n: int) -> int:
    factorial_n = 1
    for i in range(1,n+1):
        factorial_n *= i
    return factorial_n

# n! = n * (n-1) * (n-2) * ... * 1
#    = n * (n-1)!

# We could take this as a *definition* of n!:
#   0! = 1
#   n! = n * (n-1)!   when n > 0.
def factorial_rec(n: int) -> int:
    if n == 0:
        return 1
    else:
        factorial_n = n * factorial_rec(n-1)
        return factorial_n

###################################################

# General pattern for recursive functions:
#
# 1. Base case(s): simple case where we can return the answer
#    without making a recursive function call.
# 2. Recursive case(s): make some progress, reduce the problem
#    to a simpler one which can be solved recursively.

# For step 2, *ASSUME* the recursive call will give the correct
# answer to the simpler problem; what do you need to do to turn
# it into the correct answer for the original problem?

####################################################

# Compute the sum of the numbers in the given list.
def sumList(nums: List[int]) -> int:
    if (len(nums) == 0):
        return 0
    # elif (len(nums) == 1):  # unnecessary!  nums[1:] == []  if  len(nums) == 1
    #     return nums[0]
    else:
        # Simpler list: everything but the first element.
        # Assume sumList(nums[1:]) will give correct sum of nums[1:]
        # To find sum of nums, just add nums[0].
        return nums[0] + sumList(nums[1:])

# prodList(as + bs) = prodList(as) * prodList(bs)

# Compute the product of the numbers in the given list.
def prodList(nums: List[int]) -> int:
    if (len(nums) == 0):
        return 1
    # elif 0 in nums:
    #     return 0
    else:
        return nums[0] * prodList(nums[1:])

# Return a new list with the elements reversed.
def reverseList(elems: List) -> List: