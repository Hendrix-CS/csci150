# New Homework -- Loops on CodingBat

# As noted in the homework itself, you need to make a (free) account on CodingBat
# codingbat.com/python

# Project #1 is due One Week from Today. Please turn in to the Assignment on Teams

# Quiz #3 on Friday -- Function Stack Tracing

# While Loops
# Repetition!

# Syntax:
#
# while <boolean>:
#   do something
#   do something
#   do something

# At the bottom of the indented block, the code looks back at the
# <boolean> expression. If it is still true, the while loop repeats
# Otherwise, we continue below the while block



# Write a function sum_to(n) which takes in a single integer
# parameter n (which you can assume will always be non-negative)
# and returns the sum 0 + 1 + 2 + ... + n


def sum_to(n: int) -> int:
    i = 0
    s = 0
    while i <= n:
        s = s + i
        # or s += i
        i += 1

    return s




def factorial(n: int) -> int:
    i = 1
    p = 1
    while i <= n:
        p = p * i
        # or s += i
        i += 1

    return p

# now write factorial(n), which given non-negative n, finds
#  n! = 1 * 2 * 3 * ... * n.  (Note that 0! = 1, by definition).

# Generic look of while loop for counting:

# accumulator = base condition
# i = base step
# while i < (or maybe <=) some stopping condition:
#   update accumulator
#   i += 1   (or otherwise update i)
# return accumulator

# Sentinels #


# Write a function enter_value which asks the user to enter an integer between 2 and 5, inclusive
# It should repeatedly ask them until they are eventually successful

def entry() -> int:

    ans = input('Please enter an integer between 2 and 5: ')
    while not ans.isdigit() or (int(ans) < 2 or int(ans) > 5):
        ans = input('Please enter an integer between 2 and 5: ')


    numb = int(ans)
    return numb







###### We did not get to the code below here.  I'll start with the ideas below on Friday



# def entry() -> int:
#     successful = False
#     while not successful:
#         str_n = input('Enter an integer between 2 and 5, inclusive: ')
#         if str_n.isdigit(): # new command .isdigit()
#             n = int(str_n)
#             if 2 <= n <= 5:
#                 successful = True
#         else:
#             print('Please follow directions!')
#
#     return n



# This uses a 'sentinel' flag
# Basic form

# sentinel = False
# while not sentinel:
#      query the user for input
#      if input is of the correct form:
#           sentinel = True
#      else:
#           print('That is not a valid answer. Please try again.')


# Continually prompt the user to enter 'y' or 'n' -- when they do, return that value
def y_or_n() -> str:
    sentinel = False
    while not sentinel:
        ans = input('Please answer y or n ')
        if ans == 'y' or ans == 'n':
            sentinel = True
        else:
            print('I am sorry, I did not understand. Please only type (y) or (n)')

    return ans








