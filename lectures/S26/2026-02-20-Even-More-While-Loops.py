# New Homework -- Loops on CodingBat

# As noted in the homework itself, you need to make a (free) account on CodingBat
# codingbat.com/python

# Project #1 is due One Week from last Wednesday. Please turn in to the Assignment on Teams

# You also received a grade update from me by email
# -- if you have any questions or something is missing/incorrect
#    please let me know!

###### We did not get to the code below here.  I'll start with the ideas below on Friday



def entry() -> int:
    successful = False
    while not successful:
        str_n = input('Enter an integer between 2 and 5, inclusive: ')
        if str_n.isdigit(): # new command .isdigit()
            n = int(str_n)
            if 2 <= n <= 5:
                successful = True
        else:
            print('Please follow directions!')

    return n



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
    successful = False
    while not successful:
        ans = input('Please type y or n: ')
        if ans == 'y' or ans == 'n':
            successful = True
        else:
            print('I did not understand; please try again.')
    return ans














#############################
# We will write a large piece of code:
# Prompt the user to enter a positive integer (say n)
# For each 1, 2, 3, ..., n the code will
# print out the number of steps it takes to reach 1 under the Hailstone Function

# We have a lot of the pieces already written:

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

## New function:
#
#main()
# needs to ask for an integer >= 1
# for each i between 1 and n, run collatz_steps and print answer

def ask_integer():
    successful = False
    while not successful:
        str_n = input('Enter a positive integer: ')
        if str_n.isdigit():  # new command .isdigit()
            n = int(str_n)
            if n > 0:
                successful = True
        else:
            print('Please follow directions!')

    return n


def main():
    n = ask_integer()
    i = 1
    while i <= n:
        step = collatz_steps(i)
        print(f'The number {i} took {step} steps.')
        i += 1


main()