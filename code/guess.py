# guess.py is an application that plays a number guessing game with
# one computer player and one human player.
#
# Bugs: There are three bugs. Can you find them?
# YOU WILL ONLY NEED TO MAKE MINOR CHANGES/ADDITIONS TO FIX THEM!
#
# @author Gabriel Ferrer and Mark Goadrich, translated to Python 3, used classes, Nov. 2016
# @author Brent Yorgey, translated to Python 2016
# @author Valerie Summet, modified 2013
# @author Jim Skrentny, modified 2009-2012
# @author Daniel Wong, modified 2008
# @author Eva Schiffer, copyright 2006, all rights reserved

import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        self.top = random.randint(1, self.sides)

    def is_side(self, side):
        return 1 <= side <= self.sides


class Game:
    def __init__(self):
        self.die = Die(6)
        self.computer_points = 0
        self.human_points = 0
        self.round = 1
        self.max_rounds = 5
        self.num_guesses = 0

    def play_entire_game(self):
        # MAKE SURE THE PROGRAM PLAYS BY THESE RULES!!!
        print("Welcome to the Guess Game!\n\n RULES:")
        print("1. We will play five rounds.")
        print("2. Each round you will guess the number rolled on a six-sided die.")
        print("3. If you guess the correct value in three or fewer tries")
        print("   then you score a point, otherwise I score a point.")
        print("4. Whoever has the most points after five rounds wins.")

        for i in range(1, self.max_rounds):
            self.play_one_round()

        if self.computer_points > self.human_points:
            print("*** You Lose! ***")
        else:
            print("*** You Win! ***")

        print("Thanks for playing the Guess Game!")

    def play_one_round(self):
        print("\n\nROUND " + str(self.round))
        print("-------")
        self.die.roll()
        print("The computer has rolled the die.")
        print("You have three guesses.")
        
        right_guess = False
        while self.num_guesses < 3 and not right_guess:
            user_guess = int(input("\nWhat is your guess [1-" + str(self.die.sides) + "]? "))
            if self.die.is_side(user_guess):
                print("Please enter a valid guess [1-" + str(self.die.sides) + "]? ")
            else:
                if self.die.top == user_guess:
                    right_guess = True
                    print("   Correct!")
                else:
                    print("   Incorrect guess.")

                self.num_guesses += 1

        if right_guess:
            self.human_points += 1
        else:
            self.computer_points += 1
        
        print("\n*** The correct answer was: " + str(self.die.top) + " ***\n")
        print("Scores:")
        print("  You: \t\t" + str(self.human_points))
        print("  Computer: \t" + str(self.computer_points))
        print("")

        self.round += 1

def main():
    game = Game()
    game.play_entire_game()

main()
