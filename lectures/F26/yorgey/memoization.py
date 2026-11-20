# Fibonacci numbers!
#
# Start with 0, 1
# Next number is always the sum of the previous two numbers
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# Let's write a function to compute the nth Fibonacci number
#  e.g.  fib(0) = 0, fib(1) = 1, ... fib(5) = 5, fib(10) = 55, etc.
#
# Problem: fib calls itself twice every time, and ends up redoing the exact
# same work many, many times.  Exponential growth.
def fib_slow(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_slow(n - 1) + fib_slow(n - 2)

# Idea: store the answers associated with inputs we have seen in a dictionary.
# Start it out with the base cases.
fib_dict = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n not in fib_dict:
        fib_dict[n] = fib(n-1) + fib(n-2)

    return fib_dict[n]

def collatz_step(n: int) -> int:
    if n % 2 == 0:  # n is even, i.e. remainder when div by 2 is 0
        return n // 2
    else:
        return 3 * n + 1

def collatz_records_slow(upto: int):
    record = 0
    for start in range(1, upto+1):
        count = 0
        n = start
        while n != 1:
            n = collatz_step(n)
            count = count + 1

        if count > record:
            print(f"New record! {start} took {count} steps")
            record = count

steps_dict = {1: 0}

# Function to compute the number of steps n takes to reach 1.
def collatz_steps(n: int) -> int:
    if n not in steps_dict:
        steps_dict[n] = 1 + collatz_steps(collatz_step(n))

    return steps_dict[n]

def collatz_records_fast(upto: int):
    record = 0
    for start in range(1, upto+1):
        count = collatz_steps(start)
        if count > record:
            print(f"New record! {start} took {count} steps")
            record = count

def collatz_list(n: int) -> list[int]:
    nums = [n]
    while n > 1:
        n = collatz_step(n)
        nums.append(n)

    return nums