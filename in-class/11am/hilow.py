import random

repeat = "yes"
while repeat == "yes":
    print("This is the game of HIGH and LOW. The computer will pick a")
    print("random number, and you will need to guess if the next number")
    print("picked by the computer will be higher than the current")
    print("number. You get 10 chances to guess.")
    count = 0
    correct = 0
    r = random.randint(1, 10)
    while count < 10:
        print(f"The current number is {r}.")
        guess = input("Do you think the next number will be higher (yes or no)? ")
        next_r = random.randint(1, 10)
        print(f"The next number is {next_r}.")
        if (guess == "yes" and next_r > r) or (guess == "no" and next_r <= r):
            correct += 1
            print("You were right!")
        else:
            print("Sorry, you were wrong.")
        r = next_r
        count += 1
    print(f"You got {correct} out of {count} guesses correct!")
    repeat = input("Do you want to play again? ")
print("Thanks for playing!")
