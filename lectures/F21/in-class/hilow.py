import random

# Print some instructions for the user about how the game
# is played.
def print_instructions():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 3 chances to guess.")

def check_guess(user_guess: str, old_r: int, new_r: int) -> bool:
    if (user_guess == "yes" and new_r > old_r) or (user_guess == "no" and new_r <= old_r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False

def play_game() -> int:
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 3:
        print(f"The current number is {r}.")
        guess = input("Do you think the next number will be higher (yes or no)? ")
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")

        was_correct = check_guess(guess, r, next_r)
        if was_correct:
            correct += 1

        r = next_r
        count += 1
    return correct

def main():
    repeat = "yes"
    while repeat == "yes":
        print_instructions()
        correct = play_game()
        print(f"You got {correct} out of 3 guesses correct!")
        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")


main()