# Version 3:
#   - Ability to play multiple games
#   - Tell them to wrap whole game part inside a loop.

import random

# input_guess prompts the user for their guess, and keeps prompting
# until it is valid.
#
# Input:  none
# Output: a valid guess (int)
def input_guess():
    input_ok = False
    while not input_ok:
        guess_str = input("Your guess? ")
        if guess_str.isdigit():
            guess = int(guess_str)
            if guess >= 1 and guess <= 100:
                input_ok = True
            else:
                print("That is not a number between 1 and 100.  Try again.")
        else:
            print("That is not a number.  Try again.")
    return guess

def main():
    print("""Welcome to guess the number!
I will pick a number from 1-100, and you try to guess it.
I will tell you whether each guess is too low or too high.""")

    play_again = True
    while play_again:
        number = random.randint(1,100)

        print("...OK, I have picked a number.")

        guess_count = 0

        done = False
        while not done:
            guess = input_guess()
            guess_count += 1
            if guess == number:
                done = True
            elif guess < number:
                print(str(guess) + " is too low.")
            else:
                print(str(guess) + " is too high.")

        print("You got it!  It took you " + str(guess_count) + " guesses.")

        again = input("Would you like to play again? (yes/no) ")

        play_again = (again == 'yes')

main()
