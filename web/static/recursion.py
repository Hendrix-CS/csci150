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

from typing import *

def product(nums: List[int]) -> int:
    if (len(nums) == 1):
        return nums[0]
    else:
        return nums[0] * product(nums[1:])