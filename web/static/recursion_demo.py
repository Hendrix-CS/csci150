from typing import *

# Recursion!

# n! = 1 * 2 * 3 * ... * n
#
# e.g. 4! = 1 * 2 * 3 * 4 = 24
#
# By definition/convention, 0! = 1

def factorial_loop(n: int) -> int:
    pass
    # ... etc.

# A different way to compute n!
#
# Notice that   n! = (n-1)! * n

def factorial_rec(n: int) -> int:

    # Base case.
    # Think: is there a case (or cases) where I know the
    #   answer without having to do any work?
    # Write an if to test for that and return the answer.
    if n == 1:
        return 1
    else:

        # Otherwise, we want to compute the answer recursively.
        # ASSUME that factorial_rec(n-1) will give the correct answer.
        # If it does, what else do we have to do to finish computing
        # the answer for n?
        #
        # In general: call the function itself with some argument that is
        # "smaller" i.e. closer to the base case.
        return factorial_rec(n-1) * n


# Add up a list of numbers (using recursion!)
# e.g. list_sum_rec([2,5,1]) == 8.

def list_sum_rec(nums: List[int]) -> int:

    if len(nums) == 0:
        return 0
    else:
        # sum [1,4,7,9,13] = ?
        # What if we knew sum of [4,7,9,13] ?
        # Then all we would have to do is add the one remaining element.

        # ASSUME this is the correct sum of everything but the first item
        rest_sum: int = list_sum_rec(nums[1:])

        # Now finish the job:
        return nums[0] + rest_sum

        # (Could also do all on one line)

# Return the product of all the numbers in a list
# e.g. list_prod([2,5,3]) == 30
def list_prod(nums: List[int]) -> int:

    if len(nums) == 0:
        return 1
    # elif len(nums) == 1:    # Not necessary
    #     return nums[0]
    elif nums.count(0) > 0:   # Nice to have but the function would
        return 0              # still work without it
    else:
        return nums[0] * list_prod(nums[1:])

# Reverse the string s
# e.g.  reverse('abc') = 'cba'
def reverse(s: str) -> str:
    if len(s) == 0:
        return s
    # if len(s) == 1:   # unnecessary
    #     return s
    else:
        return s[-1] + reverse(s[:-1])
        # OR
        # return reverse(s[1:]) + s[0]