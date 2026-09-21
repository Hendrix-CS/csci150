#### Reminders
#
# * Homework #3 Due Today
# * Quiz Friday - Function Stack
# * Project #1 Due 1.5 week -- Wednesday, Sept 30

#
# Most class days,  I will be sharing a .py file for you to run in PyCharm
# Prior to class, a 'skeleton' of the code will be provided
# After class, I will update with the finalized version

#
#

# So far, we have talked about:
# * Input
# * Output
# * Math
# * Conditionals

# Today, we will cover Repetition

# Suppose I want to print 'Hello' 5 times.

def hello5():
    print('Hello')
    print('Hello')
    print('Hello')
    print('Hello')
    print('Hello')

# This works, but is not very efficient to code -- and not modular
#  -- what if I wanted it to print 3 times, or 8 times, or some variable number


# Better way:




# The 'while' loop

# Basic syntax:
#
# while <boolean>:
#     do some things
#     do more things

# the loop will run and then check the <boolean> condition
#   *while* it is true, the loop executes again


# Standard Example:  do some process n times

# i = 0  # this will count the step we are on -- we start counting from 0
# while i < n:  # keep going until n
#     do the thing(s)
#     i += 1   # increment i

# More examples

# Different Example Type: repeat until some condition is met

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n  +1


# Given an initial number n, we want to run hailstone until we get to 1

def collatz(n: int) -> int:
    steps = 0
    while n != 1:
        n = hailstone(n)
        steps += 1
    return steps



