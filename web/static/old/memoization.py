
# Fibonacci numbers
# F_0 = 0
# F_1 = 1
# F_n = F_(n-1) + F_(n-2)
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# Input: nonnegative int n
# Output: F_n
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# This is really slow!  The computer is doing lots of
# repeated, unnecessary, and redundant work.
#
# Idea: get the computer to remember previously
# computed values using a dictionary.
# Key = n, Value = F_n.
#
# (This is called memoization.)

fibs = {0: 0, 1 : 1}

def fib_memo(n):
    if n not in fibs:
        fibs[n] = fib_memo(n-1) + fib_memo(n-2)
    return fibs[n]

# Collatz conjecture

def hailstone(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

hailstone_lens = {}

# Input: int n
# Output: Number of iterations of 'hailstone' before reaching 1.
def hailstone_length(n):
    if n == 1:
        return 0
    elif n not in hailstone_lens:
        hailstone_lens[n] = 1 + hailstone_length(hailstone(n))

    return hailstone_lens[n]
