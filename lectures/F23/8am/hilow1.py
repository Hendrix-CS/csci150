# Function abstraction
#
# Why put our code into functions?
#
# 1. Easier to read - easier to look at things that are broken up into pieces.
# 2. Easier to debug / find problems
# 3. Reuse function instead of copy-pasting code.
# 4. Easier to test small bits of code independently of the rest of the program.

import random

def get_user_guess(old_r: int) -> bool:
    print(f"The current number is {old_r}.")
    guess = input("Do you think the next number will be higher (yes or no)? ")
    return guess == "yes"

def test_guess(user_says_higher: bool, next_r: int, old_r: int) -> bool:
    if (user_says_higher and next_r > old_r) or (not user_says_higher and next_r <= old_r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False

def pick_number() -> int:
    next_r = random.randint(1, 10)
    print(f"The next number is {next_r}.")
    return next_r

def play_once():
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 2:
        user_says_higher = get_user_guess(r)
        next_r = pick_number()
        if test_guess(user_says_higher, next_r, r):
            correct += 1
        r = next_r
        count += 1
    print(f"You got {correct} out of {count} guesses correct!")

def print_instructions():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 2 chances to guess.")

def main():
    repeat = "yes"
    while repeat == "yes":
        print_instructions()
        play_once()
        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")


main()