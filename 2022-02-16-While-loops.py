#######
# Project #1 Was Assigned today
# Look at the course webpage for more information


# Recall the 5 aspects of an algorithm:
#
#   Input
#   Output
#   Math
#   Conditionals
#   Repetition

# Today, we introduce a method for repetition

# this is the while loop:
# for example:

def while_example(n: int) -> int:
    temp = 1
    sum_so_far = 0
    while temp <= n:
        sum_so_far += temp
        temp += 1

    return sum_so_far


# a = while_example(10)
# print(a)

# In general, it is like an if statement, except that rather than going though the indented
# code only once, it does so until the boolean conditional is false:

# while <boolean>:
#   do some things
#   do some more things

# at the end of each indented block, the code jumps back to the while's conditional statement
# as long as the condition is still true, the while loop executes again
# there is no limit to the number of times that the while loop can execute

def while_input_ex() -> int:
    n = 1
    while n < 10:
        str_n = input('Enter a positive number: ')
        n = int(str_n)

    print('All done!')

#while_input_ex()


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

############ We got to here in class on Wed.
############ We will pick up with the last few lines on Friday, and then get to new information
# What if we wanted to check all numbers up to a given value?

def main2():
    print('This program will perform Hailstone and count steps up to a maximum number.')
    max_n = positive_int_input('Enter the maximum number (positive integer) you want to check: ')
    curr_n = 1
    while curr_n <= max_n:
        print('The integer ', curr_n, ' takes ', collatz_steps(curr_n), ' steps to reach 1.')
        curr_n += 1


#main2()


def y_n_input(question: str) -> str:
    is_correct = False
    while not is_correct:
        answer = input(question)

        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Please enter y or n as your answer')
