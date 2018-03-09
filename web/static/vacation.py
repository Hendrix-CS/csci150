import dictionary

# check to see if the word w has a double letter
def double_check(w):
    for i in range(len(w) - 1):
        if w[i] == w[i+1]:
            return True
    return False

# get a valid word from the user that is in the dictionary
def get_valid():
    valid = False
    while not valid:
        word = input("What do you want to bring? ")
        if not dictionary.valid_word(word, "english2.txt"):
            print("Please enter a valid English word.")
        else:
            valid = True
    return word

# get a valid word from the user that is in the dictionary
def option_input(prompt, options):
    valid = False
    while not valid:
        word = input(prompt)
        if word not in options:
            print("Please enter one of these: " + str(options))
        else:
            valid = True
    return word

def challenge(n):
    print("CHALLENGE MODE!!!")
    print("I give you " + str(n) + " words, you tell me if you can TAKE")
    print("them or must LEAVE them behind. If you are right all")
    print(str(n) + " times, you win!")

    allcorrect = True

    # give them 6 words if all correct, then they solved it!
    for i in range(n):

        # find random word
        rword = dictionary.random_valid_word("english2.txt")
        print("Word " + str(i) + ": " + rword)
        guess = option_input("Can you take it?", ["TAKE", "LEAVE"])
        if guess == "TAKE" and not double_check(rword) or \
            guess == "LEAVE" and double_check(rword):
            allcorrect = False

    if allcorrect:
        print("Hooray! You solved the puzzle!")
        solved = True
    else:
        print("You need more practice, keep trying!")


def game():
    # Tell user about the game
    print("This is the vacation game! You can try to bring things,\n"
          "and I will tell you if you can take them or not.\n"
          "You must enter English words. If you type\n"
          "CHALLENGE you will be given the opportunity to\n"
          "solve the riddle.")

    # Do this until
    solved = False
    while not solved:

        # Get input from the user
        word = get_valid()

        # see if the user wants to solve the puzzle
        if word.upper() == "CHALLENGE":
            solved = challenge(10)

        else:
            # check for double letters
            doubled = double_check(word)

            # tell them if they can bring it
            if doubled:
                print("You can take it!")
            else:
                print("Please leave that at home.")

def main():


    playagain = True
    while playagain:
        game()

        again = option_input("Do you want to play again? ", ["YES", "NO"])
        if again != "YES":
            playagain = False


main()
