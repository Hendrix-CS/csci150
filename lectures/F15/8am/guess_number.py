import random
# from random import *   -- then you can say random() instead of
#   random.random()
import math

def check_guess(guess, the_number):
    if guess > the_number:
        return "Too high!"
    elif guess < the_number:
        return "Too low!"
    else:
        return "You got it!"

def main():
    print """Welcome to guess the number! I will pick a number
    between 1 and 100 and you try to guess!"""

    the_number = int(random.random() * 100) + 1

    finished = False
    while not finished:
        guess = int(raw_input("Your guess? "))

        print check_guess(guess, the_number)
        if guess == the_number:
            finished = True

main()
