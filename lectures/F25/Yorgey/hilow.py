import random

def print_instructions():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 10 chances to guess.")

def process_guess(guess: str, r: int, next_r: int) -> bool:
    if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False

# Play the game once and return the number of correct guesses.
def play_game() -> int:
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 10:
        print(f"The current number is {r}.")
        guess = input("Do you think the next number will be higher (yes or no)? ")
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        if process_guess(guess, r, next_r):
            correct += 1
        r = next_r
        count += 1

    return correct

def main():
    repeat = "yes"
    while repeat == "yes":
        print_instructions()
        correct = play_game()
        print(f"You got {correct} out of 10 guesses correct!")
        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")

main()