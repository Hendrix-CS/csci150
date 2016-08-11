# guess.py is an application that plays a number guessing game with
# one computer player and one human player.
#
# Bugs: There are three bugs. Can you find them?
# YOU WILL ONLY NEED TO MAKE MINOR CHANGES/ADDITIONS TO FIX THEM!
#
# @author Brent Yorgey, translated to Python 2016
# @author Valerie Summet, modified 2013
# @author Jim Skrentny, modified 2009-2012
# @author Daniel Wong, modified 2008
# @author Eva Schiffer, copyright 2006, all rights reserved


import random

# YOU MAY ASSUME THE COMMENTS CORRECTLY DESCRIBE WHAT SHOULD HAPPEN.
def main():
    sides = 6                   # number of sides for a die

    user_guess = -1             # user's guess,  1 - 6 inclusive
    rolled = -1                 # number rolled, 1 - 6 inclusive
    computer_points = 0         # computer's score, 0 - 5 max
    human_points = 0            # human user's score, 0 - 5 max
    right_guess = False         # boolean flag for correct guess
    num_guesses = 0             # counts the number of guesses per round

    # MAKE SURE THE PROGRAM PLAYS BY THESE RULES!!!
    print "Welcome to the Guess Game!\n\n RULES:"
    print "1. We will play five rounds."
    print "2. Each round you will guess the number rolled on a six-sided die."
    print "3. If you guess the correct value in three or fewer tries"
    print "   then you score a point, otherwise I score a point."
    print "4. Whoever has the most points after five rounds wins."

    # BUGS ARE IN THE CODE BELOW.

    # play five rounds
    for r in range(1,5):

        # roll the die to start the round
        print "\n\nROUND " + str(r)
        print "-------"

        rolled = random.randint(1,sides)
        print "The computer has rolled the die."
        print "You have three guesses."

        # loop gives user up to three guesses
        num_guesses = 0
        while (num_guesses < 3 and not right_guess):

            # input & validation: must be in range 1 to 6 inclusive
            if (user_guess < 1 or user_guess > 6):
                user_guess = int(raw_input("\nWhat is your guess [1-6]? "))

                if ((user_guess < 1) and (user_guess > 6)):
                    print "   Please enter a valid guess [1-6]!"

            # did the user guess right?
            if (rolled == user_guess):
                right_guess = True
                print "   Correct!"
            else:
                print "   Incorrect guess."

        # if the user guessed right, they get a point
        # otherwise the computer gets a point
        if right_guess:
            human_points += 1
        else:
            computer_points += 1

        # display the answer and scores
        print "\n*** The correct answer was: " + str(rolled) + " ***\n"
        print "Scores:"
        print "  You: \t\t" + str(human_points)
        print "  Computer: \t" + str(computer_points)
        print ""

    # tell the user if they won or lost
    if (computer_points > human_points):
        print "*** You Lose! ***"
    else:
        print "*** You Win! ***"

    print "Thanks for playing the Guess Game!"

main()
