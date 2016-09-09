######
# Mark Goadrich
# CSCI 150 Fall 2016
# Vacation Game without functions
######
import random

# Requires a yes or no input
def yn_input(prompt):
    valid = False
    while (not valid):
        x = input(prompt + " (Yes or No)? ")
        if (x.lower() != "yes" and x.lower() != "no"):
            print("Please answer Yes or No.")
        else:
            valid = True
    return x.lower()

# Determines if a word contains a double letter (pp in apple)
def doubleletter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

# Determines if a word is in the wordfile provided
def valid_word(word, wordfile):
    f = open(wordfile, "r")
    for line in f:
        if line.lower().strip() == word.lower():
            return True
    return False

# Finds a random word in the wordfile
def random_valid_word(wordfile):
    f = open(wordfile, "r")
    t = f.readlines()
    r = int(random.random() * len(t))
    return t[r].strip()

# The user can challenge to see if they know the rule, they must answer n questions correctly
def challenge(wordfile, n):
    print("Challenge time!!! I will ask you " + str(n) + " questions, all of which you must answer correctly!")
    for i in range(n):
        pw = random_valid_word(wordfile)
        guess = yn_input("Q" + str(i + 1) + ": Can I take '" + pw + "' on vacation")
        if ((guess == "yes" and not doubleletter(pw)) or guess == "no" and doubleletter(pw)):
            return False
    return True

# Generates two starting words, one that matches the rule, one that doesn't
def start(wordfile):
    words = []
    while (len(words) == 0):
        pw = random_valid_word(wordfile)
        if (doubleletter(pw)):
            words.append(pw)
    while (len(words) == 1):
        pw = random_valid_word(wordfile)
        if (not doubleletter(pw)):
            words.append(pw)
    return words

# Plays the game, asking the user for words to categorize, or lets them challenge to win
def game(wordfile, n):
    print("""
Welcome to the vacation game! I'm going on vacation, and you can 
come along if you figure out the rule I'm using to pack. I will
only take certain things with me. I'll ask you what you want to take,
and then tell you if you can bring it with you. If you think you 
know the rule, type "CHALLENGE", and I'll ask you to correctly
identify 6 items. If you succeed, you are welcome on the trip!
To stop playing the game otherwise, type "QUIT".
""")

    primer = start(wordfile)
    print("To start you off, '" + primer[0] + "' is allowed, but '" + primer[1] + "' is not.")

    finished = False
    while (not finished):
        item = input("What is your item? ")
        if (item.upper() == "CHALLENGE"):
            worthy = challenge(wordfile, n)
            if (worthy):
                print("Congratulations, you can join the vacation! My rule was that " + \
                      "every item must have a double letter. (pp in apple).")
                finished = True
            else:
                print("I'm sorry, you did not get them all correct. Ask more questions!")
        elif (item.upper() == "QUIT"):
            print("Thanks for playing, come back again if you think you can figure out the rule.")
            finished = True
        elif (not valid_word(item, wordfile)):
            print("That is not a valid word, please try again.")
        else:
            takeable = doubleletter(item)
            if (takeable):
                print("Yes! You can bring that.")
            else:
                print("No, that's not allowed on this vacation.")

    # If they did not rage quit, then ask if they want to play again.
    if (item != "QUIT"):
        again = yn_input("Would you like to play again?")
        return again
    else:
        return "no"

# Repeatedly plays the game until the user is finished.
def main():
    play = True
    while (play):
        ans = game("english2.txt", 6)
        if ans == "no":
            play = False

main()
