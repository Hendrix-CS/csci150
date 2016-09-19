######
# Mark Goadrich
# CSCI 150 Fall 2016
# Vacation Game without functions
######
import dictionary_expanded

# Repeatedly plays the game until the user is finished.
wordfile = "../data/english2.txt"
play = True
while play:

    # Plays the game, asking the user for words to categorize, or
    # lets them challenge to win

    print("""
Welcome to the vacation game! I'm going on vacation, and you can 
come along if you figure out the rule I'm using to pack. I will
only take certain things with me. I'll ask you what you want to take,
and then tell you if you can bring it with you. If you think you 
know the rule, type "CHALLENGE", and I'll ask you to correctly
identify 6 items. If you succeed, you are welcome on the trip!
To stop playing the game otherwise, type "QUIT".
""")

    allowed = ""
    while allowed == "":
        pw = dictionary_expanded.random_valid_word(wordfile)
        doubled = False
        i = 0
        while i < len(pw) - 1:
            if pw[i] == pw[i + 1]:
                doubled = True
            i += 1
        if doubled:
            allowed = pw

    forbidden = ""
    while forbidden == "":
        pw = dictionary_expanded.random_valid_word(wordfile)
        doubled = False
        i = 0
        while i < len(pw) - 1:
            if pw[i] == pw[i + 1]:
                doubled = True
            i += 1
        if not doubled:
            forbidden = pw
            
    print("To start you off, '" + allowed + "' is allowed, but '" + \
          forbidden + "' is not.")

    finished = False
    while not finished:
        item = input("What is your item? ").upper()
        if item == "CHALLENGE":

            worthy = True
            print("Challenge time!!! I will ask you " + str(6) + \
                  "\nquestions, all of which you must answer correctly!")
            count = 0
            while count < 6:
                pw = dictionary_expanded.random_valid_word(wordfile)

                # Determines if a word contains a double letter (pp in apple)
                i = 0
                doubled = False
                while i < len(pw) - 1:
                    if pw[i] == pw[i + 1]:
                        doubled = True
                    i += 1

                valid = False
                while not valid:
                    guess = input("Q" + str(count + 1) + ": Can I take '" + \
                                  pw + "' on vacation (Yes or No)? ").lower()
                    if guess != "yes" and guess != "no":
                        print("Please answer Yes or No.")
                    else:
                        valid = True

                if guess == "yes" and not doubled or \
                    guess == "no" and doubled:
                    worthy = False
                count += 1
            
            if worthy:
                print("Congratulations, you can join the vacation! " + \
                      "\nMy rule was that " + \
                      "every item must have a double letter. (pp in apple).")
                finished = True
            else:
                print("I'm sorry, you did not get them all correct." + \
                      "\nAsk more questions!")

        elif item == "QUIT":
            print("Come back again if you think you can figure out the rule.")
            finished = True
            play = False

        elif not dictionary_expanded.valid_word(item, wordfile):
            print("That is not a valid word, please try again.")

        else:
            takeable = False
            i = 0
            while i < len(item) - 1:
                if item[i] == item[i + 1]:
                    takeable = True
                i += 1
            if takeable:
                print("Yes! You can bring that.")
            else:
                print("No, that's not allowed on this vacation.")

    # If they did not rage quit, then ask if they want to play again.
    if item.upper() != "QUIT":
        valid = False
        while not valid:
            again = input("Would you like to play again? " + \
                          "(Yes or No)? ").lower()
            if again != "yes" and again != "no":
                print("Please answer Yes or No.")
            else:
                valid = True
        if again == "no":
            play = False
            
print("Thanks for playing!")          
