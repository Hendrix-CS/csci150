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

# Input: a list of numbers
# Output: product of all the numbers in the list.
def product(nums):
    if (nums==[]):
        return 1
    else:
        p = nums[0] * product(nums[1:])
    return p

# Input: a string s
# Output: the reverse of s
def reverse(s):
    if s == '':
        return s
    else:
        r = s[-1] + reverse(s[:-1])
        return r

def reverse2(s):
    if len(s) <= 1:
        return s
    else:
        return reverse2(s[1:]) + s[0]

# Input: string s
# Output: whether s is a palindrome
def ispalindrome(s):
    
