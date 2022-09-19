# Reasons for using functions?
#
# 1. Code easier to read --- reduce duplication
# 2. Easier to humans read & write
# 3. Easier to figure out errors
# 4. Call a function within another function
# 5. Order doesn't matter --- independent blocks of code
# 6. Limits indentation depth
# 7. Function names help with documentation/ease of reading

import random

def main():
    repeat = "yes"
    while repeat == "yes":
        introduction()
        correct = game()
        print(f"You got {correct} out of 10 guesses correct!")
        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")

# Play the guessing game for 10 rounds and return the # of correct guesses.
def game() -> int:
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 10:
        print(f"The current number is {r}.")
        guess = input("Do you think the next number will be higher (yes or no)? ")
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        correct += is_correct(guess, next_r, r)
        r = next_r
        count += 1
    return correct

# Print an introduction to the rules.
def introduction():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 10 chances to guess.")

# Could also have this return a boolean
# See whether the guess correctly identifies whether next_r > r
# Return 1 or 0 depending on whether the guess was correct or not.
def is_correct(guess: str, next_r: int, r: int) -> int:
    if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
        print("You were right!")
        return 1
    else:
        print("Sorry, you were wrong.")
        return 0

main()