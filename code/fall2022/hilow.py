# Function abstraction

# Why use functions?

# 1. Organization - code is organized, less scattered
# 2. Reuse common sets of instructions
# 3. Easier to debug
#      - easier to find errors
#      - easier to test functions independently

import random


def welcome():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 10 chances to guess.")

# Check the user's guess, print a message, and return whether it was correct
def check_user_guess(guess: str, r: int, next_r: int) -> bool:
    if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False


# Prompt the user for their guess, and return it
def get_user_guess(r: int) -> str:
    print(f"The current number is {r}.")
    guess = input("Do you think the next number will be higher (yes or no)? ")
    return guess

def play_one_game():
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 10:
        guess = get_user_guess(r)
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        if check_user_guess(guess, r, next_r):
            correct += 1
        r = next_r
        count += 1
    print(f"You got {correct} out of {count} guesses correct!")


def play_game():
    repeat = "yes"
    while repeat == "yes":
        play_one_game()
        repeat = input("Do you want to play again? ")

def main():
    welcome()
    play_game()
    print("Thanks for playing!")

main()



# Suppose we want three things to happen: thing1, thing2, thing3.
#
# BAD:
#
# def thing1():
#   ... do some stuff ...
#   thing2()
#
# def thing2():
#   ... do some more stuff ...
#   thing3()
#
# def thing3()
#   ... does some stuff ...
#
# Not generally useful, e.g. thing3() always happens after thing2(), so we can't use them independently.

# Better:
#
# def things():
#   thing1()
#   thing2()
#   thing3()
#
# def thing1():
#    ... do some stuff ...
#
# etc.



