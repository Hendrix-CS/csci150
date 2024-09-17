# More Conditionals -- September 18, 2024
#
# Starting today, I will more often use a .py file in PyCharm
# instead of Kaggle -- you should learn to be proficient in both!
#
# A .py file is essentially one big "Code" cell
# so I will use the '#' comment character a lot in class
# to provide notes, comments, and etc
# Most "real" Python files have a lot fewer comment lines!
#
# If you haven't yet, you want to make a new Project in PyCharm:
#  * Select 'New Project' from the top menu
#  * Find/create a good folder -- I strongly recommend that you have
#       as CSCI 150 folder somewhere; make a Code From Class subfolder
#       That can be your project!
#  * You can download the code I post from class and then drag it into
#         this folder and then use it.
#  *  Try it!
#  * Once it is open in your project, right click (Mac: double finger tap)
#  * Select 'Run'

print('I was successful!')

# Reminders:
# Homework (Tracing and Coding Bat) due on Monday of next week!
# Project #1 is will be assigned on Friday! (due  Friday, October 4)
#  consider reading through the link on the webpage

##############################################

# More Practice with Conditionals

import random

def raffle() -> str:
    chance = random.random()  # a float between 0 and 1


    if chance < 0.6:
        return 'You get a $2 coupon!'
    if 0.6 <= chance < 0.95:
        return 'You get a candy bar!'
    if chance >= 0.95:
        return 'Your purchase is free!!'

# You have two options for running a .py file through PyCharm:
#  * 'Regular' Run -- click on the green triangle at the top or right click
#       and select Run -- this runs the entire file once and quits
#  * Run in the Python Console -- right click and select 'Run File in Python Console'
#      this runs the file, but then does NOT quit and allows you to access any function
#      or variable you stored in memory!

def raffle2() -> str:
    chance = random.random()

    if chance < 0.6:
        return '$2 coupon.'
    elif chance < 0.95:
        return 'Candy bar.'
    else:
        return 'Free purchase'

##
def big(a :int) -> str:
    b = input('Enter an integer: ')
    b = int(b)
    if a < b:
        return 'Wow! Your number was big!'
    else:
        return 'That is not a very big number.'


def str_order() -> str:
    s = input('Enter a string: ')
    t = input('Enter another string: ')
    if s < t:
        return s
    elif s == t:
        return 'Equal!'
    else:
        return t


## Time for Quiz!
