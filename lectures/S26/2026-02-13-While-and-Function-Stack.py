# Reminders
# Quiz #2 Today -- Booleans and Conditional
# Homework #3 (Function Stack Tracing) *Wednesday*
# Project #1 is assigned -- due Wed Feb 25

# Function Stack -- last example from Wednesday

def aaa(x: int, s: str) -> int:
    z = 7
    if x < z and s < 'hello':
        z += 3
        print(f'My string is {s} and number is {x}.')
    else:
        z *= 4
        print(f'I do not like the number {x}.')
    return z

def bbb(x: int, y: int) -> int:
    if x < y:
        return y // x
    else:
        return x - y

def main3():
    x = bbb(7,2)
    print(aaa(x,'hi'))
    print(aaa(bbb(3,14),'abcd'))

#main3()


##################################
# Recall the Hailstone Function:

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

# The Collatz Conjecture is that no matter what number you start with,
# you will eventually reach 1

# We previously saw that the hailstone function needed conditionals:
# * do one thing for evens and something else for odd
#
# What we need now is *repetition*
# Continue to perform some action until we don't want to anymore


def print_loop(n: int):
    i = 0
    while i < n:
        print(i)
        i += 1


def sum_to_n(n: int) -> int:
    s = 0
    i = 0
    while i < n:
        s = s + i
        i += 1

    return s


def collatz(n: int) -> int:
    steps = 0
    while n != 1:
        n = hailstone(n)
        steps += 1
    return steps