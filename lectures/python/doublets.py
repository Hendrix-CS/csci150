# 9 March 2016
# Doublets!

import dictionary

# Copied from class
#
# Inputs:
#   - prompt: string to be used as a prompt.
# Output: int typed by the user
#
# Repeatedly prompts the user until the enter an int.
def int_input(prompt):
    valid_input = False
    while valid_input == False:
    # while not valid_input:
        user_input = raw_input(prompt)
        valid_input = user_input.isdigit() or\
                      (user_input[0] == '-' and user_input[1:].isdigit())
        if not valid_input:
            print "That's not an int, try again!"
    return int(user_input)

# Inputs:
#   - prompt: string to be used as a prompt.
#   - the_string: string we want an index into
# Outputs: valid index into the_string
#
# Repeatedly prompt the user until they enter a
# valid index for the_string.
def index_input(prompt, the_string):
    valid_input = False
    while not valid_input:
        user_input = int_input(prompt)
        valid_input = user_input >= 0 and user_input < len(the_string)
        if not valid_input:
            print "That's not a valid index into " + the_string +\
                     ", enter a number between 0 and " + str(len(the_string) - 1)
    return user_input

# Input: a description of which word is wanted
# Output: a valid word
#
# Prompt the user for a valid English word.
def get_word(which_word):
    is_valid = False
    while not is_valid:
        user_input = raw_input("Enter the " + which_word + " word: ")
        if dictionary.valid_word(user_input, "english2.txt"):
            is_valid = True
        else:
            print user_input + " is not a word.  Try again."
    return user_input

# Input: none
# Output: string
#
# Prompt the user for a valid English word.
def get_start_word():
    return get_word('starting')

def get_end_word(start):
    same_length = False
    while not same_length:
        user_word = get_word('ending')
        if len(user_word) == len(start):
            same_length = True
        else:
            print user_word + " is not the same length as " + start + ". Try again."
    return user_word

# Input:
#   - string word
#   - index: int, must be a valid index into word
#   - new_letter: character
#
# Output: word with the index position replaced by new_letter
def replace_letter(word, index, new_letter):
    return word[:index] + new_letter + word[index+1:]

def play_game(start, end):
    print "Playing!"

def main():
    start = get_start_word()
    end = get_end_word(start)
    play_game(start, end)
