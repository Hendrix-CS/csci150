# Version 1:
#   - tell them to make a main() and call it @ the end
#   - pick a random number
#   - loop until they get it right  (can either use sentinel, or use guess as condition)
#   - count number of guesses

import random

def main():
    print("""Welcome to guess the number!
I will pick a number from 1-100, and you try to guess it.
I will tell you whether each guess is too low or too high.""")

    number = random.randint(1,100)

    print("...OK, I have picked a number.")

    guess_count = 0

    done = False
    while not done:
        guess = int(input("Your guess? "))
        guess_count += 1
        if guess == number:
            done = True
        elif guess < number:
            print(str(guess) + " is too low.")
        else:
            print(str(guess) + " is too high.")

    print("You got it!  It took you " + str(guess_count) + " guesses.")

main()
