#### Reminders
#
# * Homework #4 Assigned Today (see below)
# * Quiz Friday - Function Stack
# * Project #1 Due in one week -- Wednesday, Sept 30

# Homework #4 --
# In addition to paper & pencil homework, you'll be using CodingBat
# You can go to https://codingbat.com/python
# and make a free account -- please use your Hendrix email as your ID
# password can be whatever you like
# Under 'pref' menu, put my email (seme@hendrix.edu) in the 'Teacher Share' box!

# Let's do more examples of using a while loop:

def factorial(n) -> int: # returns n! (5! = 5 * 4 * 3 * 2 * 1), for example
    ans = 1
    i = 1
    while i <= n:
        ans *= i
        i += 1
    return ans


def add_evens(n: int) -> int:  # will return the sum of the non-negative even integers < n
    total = 0
    i = 0
    while i < n:
        if i % 2 == 0:
            total += i

        i += 1

    return total

# write function add_up which prompts the user to enter an integer
# when it keeps a running total, and stops when they enter 0

# Initially we wrote this version
# def add_up() -> int:
#     total = 0
#     num = int(input('Please enter an integer () to stop): '))
#
#     while num != 0:
#         total += num
#         num = int(input('Please enter an integer () to stop): '))
#
#     return total

# We then wrote the version below, which is mre robust against poor user input
# -- i.e. typing a letter or something.
# However, it does not currently work for negatives.  We will fix this
# next week.

def add_up() -> int:
    total = 0
    num = enter_integer()

    while num != 0:
        total += num
        num = enter_integer()

    return total


# New built-in function: .isdigit()
# s.isdigit() will return True if the string s contains *only* 0, 1, 2, ..., 9 as characters

def enter_integer() -> int:
    success = False

    while not success:
        ans = input('Enter a positive integer: ')
        if ans.isdigit():
            num = int(ans)
            success = True
        else:
            print('I did not understand. Please try again.')

    return num



# This is an example of a 'sentinel' while loop --
#    it repeats asking for information (in this case, an integer)
#    until the user correctly does so
