# Computer guess version.
# Hints:
#   - make a main.
#   - don't worry about making other functions.
#   - get one game working first.  Then wrap in a play again loop.
#   - Detecting cheating is optional.

def main():
    print("""Welcome to guess the number!  You pick a number from 1-100
and I will guess it.  Please tell me whether my guesses are
"correct", "low", or "high".""")

    play_again = True
    while play_again:
        correct = False
        low = 1
        high = 100

        guess_count = 0

        while not correct and low <= high:
            guess = (low + high)//2
            guess_count += 1
            result = input("Is your number " + str(guess) + "? ")
            if result == "correct":
                correct = True
            elif result == "low":
                low = guess + 1
            elif result == "high":
                high = guess - 1
            else:
                print('Please respond with "correct", "low", or "high".')

        if correct:
            print("Yay!  I win!  It only took me " + str(guess_count) + " guesses.")
        else:
            print("You are a cheater!!")

        again = input("Shall we play again? (yes/no) ")
        play_again = (again == 'yes')

main()
