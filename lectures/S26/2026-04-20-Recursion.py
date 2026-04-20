# Reminders
# * No Quiz this week
# * Homework assigned today for Recursion -- due Monday
# * Quiz next Friday (Recursion)

# This week -- Recursion
# Next week:
# * Monday -- final topics
# * Wed/Fri work on final project
# Fri - take last quiz, and can make up other quizzes, possibly.

# RECURSION

# "In order to understand recursion, one my first understand recursion."

# Consider the follow function:

def f(n: int) -> int:
    if n == 0:
        return 0
    else:
        return 1 + f(n - 1)

# Run in the console for a few values of n

# Notice that the function f calls *itself*

def list_sum(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])


# # Look at the structure of the code we just analyzed
# # It has an if statement -- if len(lst) == 0
# #   This is the "base" case, or the escape clause
# #   It is the situation at the bottom of the pile
# # The else line is the one that calls the function itself again
# #  It is called the "recursive case"
# #     In order to sum the entries in a list, you simply add the
# #     first element of the list to the result of the sum of the remainder of the list

# That is, the *base case* is the simplest situation, or the one whose answer we know without thinking

#The *recursive case* is where we take a situation and simplify it -- make it shorter or smaller or...

# #  The most likely place you have seen this for real in the past is the factorial function:
# #  5! = 5 * 4 * 3 * 2 * 1





# #  but notice that we can write 5! = 5 * (4!) -- that is we can write a factorial
# # in terms of a simple operation involving a smaller case.


def factorial(n: int) -> int:
    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)



def f_while(n: int) -> int:
    s = 0
    i = 0
    while i < n:
        s += 1
        i+=1
    return s












# There are lots of recursive ideas in mathematics and comptuer science, beyond "simple" arithmetical operations

# Ex: When is a word a palindrome?
# When the first and last characters agree and the middle is also a palindrome

# Fractal Images
#

# Trees (real and as a formal idea)

# Search -- maze solutions,

# Many repetitive processes can be thought of recursively

# File structure on a computer -- Folders, which contain folders, which contain ...


# Do not do the following, however!
def y_n_bad() -> bool:
    ans = input('Enter yes or no. ')
    if ans == 'yes':
        return True
    elif ans == 'no':
        return False
    else:
        y_n_bad()