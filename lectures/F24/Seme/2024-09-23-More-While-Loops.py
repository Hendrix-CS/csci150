# New Homework -- Loops on CodingBat

# Write a function sum_to(n) which takes in a single integer
# parameter n (which you can assume will always be non-negative)
# and returns the sum 0 + 1 + 2 + ... + n

# For example, sum_to(5) = 15, since 0  + 1 + 2 + 3 + 4 + 5 = 15

# now write factorial(n), which given non-negative n, finds
#  n! = 1 * 2 * 3 * ... * n.  (Note that 0! = 1, by definition).

# Generic look of while loop for counting:

# accumulator = base condition
# i = base step
# while i < (or maybe <=) some stopping condition:
#   update accumulator
#   i += 1   (or otherwise update i)
# return accumulator


###############
# Again, input checking
# Write a function enter_value which asks the user to enter an integer between 2 and 5, inclusive
# It should repeatedly ask them until they are eventually successful

# This uses a 'sentinel' flag
# Basic form

# sentinel = False
# while not sentinel:
#      query the user for input
#      if input is of the correct form:
#           sentinel = True
#      else:
#           print('That is not a valid answer. Please try again.')

# Context -- for today, we'll look at an old problem, the Collatz Conjecture:
# Given any positive integer, does the Hailstone function eventually reach 1?
# and if so, for each starting number, can we report back the number of steps.

# Let's plan this out:

# Query user for a positive integer
# Repeat until you get to 1:
#      run Hailstone
#      add one to the number of steps
# report back to the user the number of steps

# What functions might we use?
# A query user -- ask them what number they want to check
# hailstone -- which we have written before!
# a step-counter wrapper



# We will use the isdigit() built in function:
# <str>.isdigit() returns True whenever <str> is made up of only digits 0, 1, ..., 9
# if the string contains a negative, a decimal, or any other non-digit character
# it returns False



def positive_int_input(question: str) -> int:
    is_ok = False  # this is called a `sentinel' value
    while not is_ok:
        n = input(question) # remember that input thinks of its value as a string!

        if n.isdigit():
            is_ok = True
        else:
            print('That is not a positive integer. Please try again.')

    return int(n)


def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = hailstone(n)
        steps += 1

    return steps


# We use a 'main' as the central control for our program

def main():
    init_n = positive_int_input('Please enter a positive integer to count Hailstone steps: ')
    steps = collatz_steps(init_n)
    print(f'The integer {init_n} takes {steps} steps to reach 1.')


main()




