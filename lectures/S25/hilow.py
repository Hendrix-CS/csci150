import random

def intro():
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 10 chances to guess.")

def get_user_guess(r: int) -> str:
    print(f"The current number is {r}.")
    guess = input("Do you think the next number will be higher (yes or no)? ")
    return guess

def check_user_guess(r: int, next_r: int, guess: str) -> bool:
    if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
        print("You were right!")
        return True
    else:
        print("Sorry, you were wrong.")
        return False

def play_game():
    intro()
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 10:
        guess = get_user_guess(r)
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        if check_user_guess(r, next_r, guess):
            correct += 1
        r = next_r
        count += 1
    print(f"You got {correct} out of {count} guesses correct!")

def main():
    repeat = "yes"
    while repeat == "yes":
        play_game()
        repeat = input("Do you want to play again? ")
    print("Thanks for playing!")

main()


# DON'T have each function call a function that should happen next.
#
# def f1():
#    do stuff
#    f2()
#
# def f2():
#    do more stuff
#    f3()
#
# def f3():
#    yet more stuff
#
# BETTER:
#
# def main():
#   f1()
#   f2()
#   f3()
#
# def f1():
#   do stuff