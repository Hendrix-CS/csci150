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

# Input: list of ints
# Output: product of all the numbers in the list (int).
def listprod(nums):
    if nums == []:
        


####################################

# Thought process to write factorial_rec function!

# 1. Write inputs/outputs!

# Input: n (int)
# Output: an int which is the factorial of n (1 * 2 * 3 * ... * n)
#   Note that 0! = 1.
def fact(n):
    # 2. Think of simple cases for the input ("base cases") where
    #   we can return the answer immediately.
    if n == 0:
        return 1
##    elif n == 1:   # this base case is unnecessary
##        return 1

    else:
        # 3. What if I knew the answer to a simpler problem?
        # e.g. fact(n-1) ?
        #
        # "Leap of faith": ASSUME that fact(n-1) will work correctly.
        # If it does, how can we use its answer to compute the
        # correct output to fact(n) ?
        #
        # In this case: we need to multiply fact(n-1) by n.
        return n * fact(n-1)
