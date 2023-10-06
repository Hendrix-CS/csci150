# Function abstraction
#
# What are the benefits of structuring programs using functions?
#
# 1. Better organization, easier to find problems
# 2. Easier to read, understand, & modify.
# 3. The above two points are especially important for collaboration.
# 4. Easier to individually test small pieces of code by putting them in functions.
# 5. Allows us to avoid repeating/copy-pasting the same code over and over.

import random

def print_intro():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 2 chances to guess.")

def get_user_guess(cur_r: int) -> bool:
    print(f"The current number is {cur_r}.")
    guess = input("Do you think the next number will be higher (yes or no)? ")
    return guess == "yes"

def check_guess(user_says_higher: bool, next_r: int, old_r: int) -> bool:
    if (user_says_higher and next_r > old_r) or (not user_says_higher and next_r <= old_r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False

def play_game():
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 2:
        user_says_higher = get_user_guess(r)
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        user_was_correct = check_guess(user_says_higher, next_r, r)
        if user_was_correct:
            correct += 1
        r = next_r
        count += 1
    print(f"You got {correct} out of {count} guesses correct!")

def main():
    repeat = "yes"
    while repeat == "yes":
        print_intro()
        play_game()
        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")


main()