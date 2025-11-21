# More recursion examples

# Fibonacci numbers:
#   - start with 0, 1
#   - each number is the sum of the previous two
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# fib(n) = the nth Fibonacci number.
def fib_slow(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_slow(n - 1) + fib_slow(n - 2)

# We can use a dictionary to remember output values of fib(n) for each n,
# so we can avoid redundant recalculations.

fib_dict = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n in fib_dict:      # look up fib(n) if it is already in the dictionary
        return fib_dict[n]
    else:
        # Calculate fib(n) and fill in the dictionary
        fib_dict[n] = fib(n-1) + fib(n-2)

        return fib_dict[n]

