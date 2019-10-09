import random

def introduction(num_guesses: int):
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print(f"number. You get {num_guesses} chances to guess.")

def determine_correct(guess: str, next_r: int, r:int):
    if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
        print("You were right!")
        return 1
    else:
        print("Sorry, you were wrong.")
        return 0

def yes_no_answer(prompt: str) -> str:
    finished = False
    while not finished:
        answer = input(prompt)
        if answer == "yes" or answer == "no":
            finished = True
        else:
            print("Please answer yes or no.")
    return answer

def game(num_guesses: int, upper: int) -> int:
    count = 0
    correct = 0
    r = random.randint(1, upper)
    while count < num_guesses:
        print(f"The current number is {r}.")
        guess = yes_no_answer("Do you think the next number will be higher (yes or no)? ")
        next_r = random.randint(1, upper)
        print(f"The next number is {next_r}.")
        correct += determine_correct(guess, next_r, r)
        r = next_r
        count += 1
    return correct

def main():
    num_guesses = 5
    upper_bound = 30
    repeat = "yes"
    while repeat == "yes":
        introduction(num_guesses)
        correct = game(num_guesses, upper_bound)
        print(f"You got {correct} out of {num_guesses} guesses correct!")
        repeat = yes_no_answer("Do you want to play again? ")
    print("Thanks for playing!")

main()
