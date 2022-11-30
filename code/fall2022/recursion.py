# Example:
# Compute n factorial, i.e. n! = 1 * 2 * 3 * ... * n

# We could do this with a loop:
def fac_loop(n: int) -> int:
    prod: int = 1
    for k in range(1,n+1):
        prod *= k
    return prod

# A different way!  Notice that
#   n! = n * (n-1) * ... * 3 * 2 * 1
#      = n * (n-1)!
#
# For this to be a viable *definition* of n!, we have to also include a stopping point:
#
# 0! = 1
#
# Can we directly turn this into Python code?
#
# 0! = 1
# n! = n * (n-1)!

def fac_rec(n: int) -> int:
    if n == 0:      # "base case": simple case where we know the answer without calling the function again.
        return 1    # ensures the function will eventually stop.
    else:
                    # recursive case: calls itself on a *simpler* (smaller, shorter, ...) input.
                    # Given a correct result for the simpler case, it then constructs the correct
                    # answer for the original input.
        return n * fac_rec(n-1)

from typing import *

# Example: sum of a list.
def list_sum(nums: List[int]) -> int:
    # Base case:
    if nums == []:
        return 0
    else:
        # Make a recursive call on a slightly simpler input, ASSUME (leap of faith)
        # that it will give the correct answer!
        #
        # e.g. if we had lst = [1,2,3],  this will give  sum_rest = list_sum([2,3]) = 5
        sum_rest = list_sum(nums[1:])
        # Now turn it into the answer to the original problem
        # In this case, just add that first element.
        return nums[0] + sum_rest

# Is a string a palindrome?  i.e. is it the same forward and backward?
def is_palindrome(s: str) -> bool:
    # Base case:
    if len(s) <= 1:  # empty string or single character
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
