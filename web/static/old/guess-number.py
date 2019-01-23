# 17 Feb, 2016
# Guess the number!

# Computer should pick a random number
# Human gets to guess.

import random

print """Welcome to guess-a-number! I'm thinking
of a number between 1 and 100. Etc."""

the_number = random.randint(1,100)

# Just for testing -- we'll delete it later
# print "Psst, the number I picked is", the_number

guess = -1

while guess != the_number:

    guess = int(raw_input("What is your guess? "))

    if guess > the_number:
        print "Too high!"
    elif guess < the_number:
        print "Too low!"
    else:
        print "You got it!"

