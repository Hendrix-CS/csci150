# Project 2 demo
# Doublets!

import dictionary

def pick_start_word():
    valid = False
    while not valid:
        start = input("Please choose a starting word: ")
        if (not dictionary.valid_word(start, 'english2.txt')):
            print ("That's not a word! Try again.")
        else:
            valid = True
    return start

def pick_end_word():
    return 'golf'

def chain_words(start, end):
    print ("You have to get from " + start + " to " + end)

def play_game():
    start = pick_start_word()
    end   = pick_end_word()
    chain_words(start, end)

# Inputs: none
# Output: True if the user is done
def is_user_done():
    done_str = input("Do you want to play again? (y/n) ")
    return (done_str == 'n')  

def main():
    done = False
    while not done:
        play_game()
        done = is_user_done()

main()
