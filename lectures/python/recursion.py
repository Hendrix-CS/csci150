# 11 March 2016
# Recursion!

# Basic idea: function that calls itself.
# Works if the calls keep getting closer to some
# "base case" or stopping point.

# Factorial: n! = 1 * 2 * 3 * ... * n
def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

# Compute factorial recursively.
def factorial_rec(n):
    # 1. Base case(s): inputs for which we know the
    # answer immediately without making a
    # recursive call.
    if (n == 0):
        return 1
    else:
        # Make recursive call(s) to solve *simpler* problems.
        # "Leap of faith": trust that they give the right answer
        # Combine the answer(s) to yield the overall answer.
        return factorial_rec(n-1) * n

# Input: a list of numbers
# Output: sum of the list.
def our_sum(nums):
    if (nums == []):
        return 0
    # base case for len = 1??
    else:
        s = nums[0] + our_sum(nums[1:])
        return s


