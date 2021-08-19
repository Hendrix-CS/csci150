from typing import *

# Recursion!

# Recall n! ("n factorial") = 1 * 2 * 3 * ... * n
# How can we write a Python function to compute n! ?

# We could write this as a loop:
def fac_loop(n: int) -> int:
    prod: int = 1
    for k in range(1,n+1):
        prod *= k
    return prod

# Consider that
#   n! = n * (n-1) * (n-2) * ... * 1
#      = n * ((n-1) * (n-2) * ... * 1)
#      = n * (n-1)!
#
# We could actually *define* factorial this way:
#   0! = 1
#   n! = n * (n-1)!

# We can write a Python function that corresponds
# directly to this definition.

# Assume n >= 0.
def fac_rec(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fac_rec(n-1)

# How to think about writing a recursive function?
#
#   1. Base case(s). What are the simple cases in which
#      you immediately know the answer without doing more work?
#   2. Recursive case: big idea: transform the problem
#      into a slightly simpler version of the problem,
#      and then do a bit of work to transform the answer
#      to the simpler problem into the answer for the
#      whole problem.

def fac_rec2(n: int) -> int:
    # Step 1: base case(s)
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        # We have to compute n!
        # A simpler version of the problem is to
        #   compute (n-1)!.

        # Call fac_rec on (n-1) and ASSUME (via a leap of faith)
        #   that it will give the correct answer!

        fac_n_minus_1 = fac_rec2(n-1)

        # What do we have to do to get n! if we know (n-1)! ?
        #   Just multiply by n.

        return n * fac_n_minus_1

# Multiply a list of numbers and return their product.
def list_product(nums: List[int]) -> int:
    if 0 in nums:
        return 0
    # elif len(nums) == 1:
    #     return nums[0]
    elif len(nums) == 0:
        return 1
    else:
        prod_rest = list_product(nums[1:])
        return nums[0] * prod_rest