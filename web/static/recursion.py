from typing import *


# Factorial function.  n! = 1 * 2 * 3 * ... * n

def factorial_loop(n: int) -> int:
    result: int = 1
    for i in range(1,n+1):
        result *= i
    return result


# A different way to implement factorial:
#
# n! = n * (n-1) * (n-2) * ... * 1
#    = n * ((n-1) * (n-2) * ... * 1)
#    = n * (n-1)!
#
# If we also observe that 0! = 1, we can take this as a
# *definition* of factorial:
#
# 0! = 1
# n! = n * (n-1)!   (if n > 0).
#
# Can we turn this directly into Python code?

def factorial(n: int) -> int:

    # "Base case": simple case where it knows
    # the answer without having to call itself

    if n == 0:
        return 1
    else:

        # Recursive case:
        #   1. Call itself with a simpler (closer to the base case).
        #   2. Assume that the recursive call gives the correct answer
        #   3. Use the answer from the recursive call to compute
        #      the overall answer.
        return n * factorial(n-1)


# Another example: list product

def product(nums: List[int]) -> int:
    if len(nums) == 0:
        return 1
    # elif len(nums) == 1:   # unnecessary!
    #     return nums[0]
    else:
        return nums[0] * product(nums[1:])


# Add up all the numbers in a list

def sum(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum(nums[1:])


# Return the reverse of a string (recursively).
#
# e.g.  reverse('stressed') = 'desserts'
def reverse(word: str) -> str:
    if len(word) == 0:
        return ''
    else:
        return word[-1] + reverse(word[:-1])

