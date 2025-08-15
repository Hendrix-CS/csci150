# Fibonacci numbers
#
# Start with 0,1.  At each step, add the two previous numbers to get the next number.
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# Let's write a Python program to compute the nth Fibonacci number.
# Sadly, it is slow since it does lots of redundant work!!
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Better version: save previous results in a dictionary and don't recompute them again

fib_dict = {0: 0, 1: 1}

def fib2(n: int) -> int:
    if n not in fib_dict:
        fib_dict[n] = fib2(n-1) + fib2(n-2)

    return fib_dict[n]

# Collatz function

# collatz_dict[n] = number of steps to reach 1 starting from n
collatz_dict = {1: 0}

def step(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def collatz_steps(n: int) -> int:
    if n not in collatz_dict:
        collatz_dict[n] = 1 + collatz_steps(step(n))

    return collatz_dict[n]

max_steps = 0
max_n = 0
for n in range(1, 10000001):
    steps = collatz_steps(n)
    if steps > max_steps:
        max_steps = steps
        max_n = n

print(f'Most steps was {max_steps} starting from {max_n}')