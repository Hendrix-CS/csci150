# Recursion!

# Factorial

# n! = 1 * 2 * 3 * ... * n

# Input: a nonnegative integer n
# Output: n!
def factorial(n):
    count = 0
    product = 1
    while count != n:
        count += 1
        product *= count
    return product

def factorial2(n):
    product = 1
    for count in range(1,n+1):
        product *= count
    return product

# n! = (n-1)! * n
# 0! = 1

# The above is a valid definition of factorial.  Can we turn
# it directly into Python code?

def factorial_rec(n):
    if n == 0:
        return 1
    else:
        result = n * factorial_rec(n-1)
        return result

# Input: list of ints
# Output: sum of the list.
def listsum(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + listsum(nums[1:])




        

