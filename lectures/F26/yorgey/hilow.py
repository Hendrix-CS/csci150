import random

# Check the user's guess, print a message, and return whether the guess was correct
def check_user_guess(guess: str, r: int, next_r: int) -> bool:
    if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False


def play_game():
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 10:
        print(f"The current number is {r}.")
        guess = input("Do you think the next number will be higher (yes or no)? ")
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        if check_user_guess(guess, r, next_r):
            correct += 1
        r = next_r
        count += 1
    print(f"You got {correct} out of {count} guesses correct!")

def print_instructions():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 10 chances to guess.")

def main():
    repeat = "yes"
    while repeat == "yes":
        print_instructions()
        play_game()

        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")

main()