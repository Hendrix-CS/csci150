from typing import *


# Correct implementation of input checker
def input_check() -> bool:
    is_okay = False
    while not is_okay:
        answer = input('Enter yes or no').lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('That is not a valid response. Try again.')



# Not a correct implementation -- though an understandable idea
def input_check2() -> bool:
    answer = input('Enter yes or no').lower()
    if answer == 'yes':
        return True
    elif answer == 'no':
        return False
    else:
        print('That is not a valid response. Try again.')
        input_check2()


# This file will introduce you to the idea of recursion
# We first start with a review, however, of loops

# Given a list of integers, write a function list_sum which will return the sum of the list
# if the list is empty, it should return 0

# this can be done in a number of ways:

# while loop
# you should think about how you might do this before looking ahead!



















def list_sum_while(lst: List[int]) -> int:
    sum = 0
    i = 0
    while i < len(lst):
        sum += lst[i]
        i += 1
    return sum










# for loop version -- looping directly over the entries
# again, take a moment on paper or in PyCharm / notebook on your own to try it!


def list_sum_for(lst: List[int]) -> int:
    sum = 0
    for item in lst:
        sum += item

    return sum








#
# for loop, using range
# you can alternatively loop over the list using the range operation
# again please try this!



















def list_sum_range(lst: List[int]) -> int:
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum












#
#
#
# #for loop version - looping with range



# Now go back and run this file in the console.  Come up with a few of your own lists and
# see that they should all hopefully produce the same result.
# There is nothing inherently better / worse about one implementation than another,
# though I'll argue that the direct for loop is likely the easiest to do without mistakes














# Now look at the following code:
def list_sum(lst: List[int]) -> int:
    if len(lst) == 0: # 'base case' -- what to do in the simple case
        return 0
    else: # the 'recursive case' -- how to take our problem, and make it simpler
        return lst[0] + list_sum(lst[1:]) # the recursive case always calls the function itself, but
                # on a smaller list, smaller number, simpler situation

# run this on a few sample lists
# does it produce the correct value for the sum?

# Let's look at how it traces



# Look at the structure of the code we just analyzed
# It has an if statement -- if len(lst) == 0
#   This is the "base" case, or the escape clause
#   It is the situation at the bottom of the pile
# The else line is the one that calls the function itself again
#  It is called the "recursive case"
#     In order to sum the entries in a list, you simply add the
#     first element of the list to the result of the sum of the remainder of the list

#  The most likely place you have seen this for real in the past is the factorial function:
#  5! = 5 * 4 * 3 * 2 * 1
#  but notice that we can write 5! = 5 * (4!) -- that is we can write a factorial
# in terms of a simple operation involving a smaller case.



# n! = n * (n - 1)!
# base case -- 0! = 1

def recursive_factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

#  This is where recursion comes in:

# The following function returns n!, for non-negative integers n
# def recursive_factorial(n: int) -> int:
#
#     # base case -- for factorial, we define 0! = 1
#     if n == 0:
#         return 1
#     else:
#         return n *  recursive_factorial(n - 1)
#
#
# # Trace this for recursive_factorial(4)
#
#
