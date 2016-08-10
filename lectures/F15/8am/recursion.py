# Recursion
#
# Recursion = a function that calls itself
#
# Idea: transform a problem into a slightly simpler version(s),
#   solve those by calling the function recursively,
#   then do a little bit of work to solve the original problem.

# Factorial function: n! = 1 * 2 * 3 * ... * n

# Iterative version:
def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

# Recursive version:
# 0! = 1
# n! = (n-1)! * n  (when n > 0)
def fact_rec(n):

    # 1. "base case(s)": simple case where you know the answer without
    #   doing any extra work.
    if n == 0:
        return 1

    # 2. "recursive case(s)": reduce the problem to a simpler problem,
    #   solve it recursively, and do some work to find the final
    #   answer
    else:
        result = fact_rec(n-1) * n
        return result

# Fibonacci numbers
# F_0 = 0
# F_1 = 1
# F_n = F_(n-1) + F_(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
