from typing import *
import random

# Function Abstraction

# We have been writing a lot of small functions that do small tasks
#
# Though some of that is because this is an intro level course,
# it is also true that most programming takes place at the small function,
# small individual task level

# Benefits:
# Easier to debug
# Easier to understand
# Often can reuse already-written code
# Easier to modify/update as needed

# Function Abstraction -- big picture: assume each small function
# works correctly. How do the pieces fit together?
# In fact *what* pieces are even needed?

# Modularity -- breaking complicated tasks into small, manageable chunks
# Very rarely should a function be more than 15-20 lines or so long
# (this is not a hard and fast rule)

# Generic Rules:
#
# Each overall program should have a single main()
# main() is the traffic cop -- directs other functions
# main() should *never* return anything (though it might print)
# no other function should *ever* call main
#   -- if you think you have an exception to these rules, ask me

# if main() calls some function f1():
# -- f1() will eventually go back to main:
#    -- if f1() returns a value, that value is only returned to main()
#         (of course, not every function returns something)
#    -- if f1() calls g1(), g1() will eventually go back to f1()
#        -- not to main()
#    -- if g1 calls some h1(),  h1() goes back to g1(), which
#               goes back to f1(), which goes back to main()

# each function should have a single, simple task to complete
# which you should be able to describe in a sentence or so
#
# if you find yourself saying "it calculates area *and* then also calculates..."
#   you really have two functions, almost certainly

#############################################################
#############################################################
# Example #
#
# This will also serve as an example of the flow of a simple game
# -- so quite useful for Project #2!!
#############################################################
#############################################################

# Code Breaker
#
# We are going to write a simple human vs computer game
# The computer makes up a code using the six letters A, B, C, D, E, F
# of length 3, 4, or 5
# Human player tries to guess
# For each guess, computer awards human an 'X' if a guessed letter
# is in the correct position and an 'o' is they have a correct letter
# but in the wrong position.
# They receive '_' for incorrect guesses.

#
# For example:
# Code = 'ABAE'
# Guess ='CBBA'
# key =  'Xo__'

# Before we began, we played 2 versions "live" on the board

# Outline of tasks:

# main -- control
#   print rules
#   select length of code
#   play game ** more detail to come
#   play again?

#   play game
#      have computer make up code
#      loop
#         human guesses
#         make key
#         update status
#         end game if guess is correct or out of turns

# And now, the code
def print_rules():
    print('Hello and welcome to Code Breaker -- based on the 1970s sensation Mastermind')
    print('The human chooses a level to play.')
    print('The computer will choose a code of a given length, using the characters: A, B, C, D, E, F')
    print('The human guesses, and then is given a key:')
    print('   They get an "X" for each letter in the correct spot')
    print('   They get an "o" for each letter that is in the code, but wrong place.')
    print('You will have 12 total guesses')
    input('Hit "enter" when you are ready to play!')

# this function sets the difficulty level
# Notice that I have only encoded the length in *one* place
# This makes is very easy to change
def set_level() -> int:
    easy = 3
    medium = 4
    hard = 5
    print('This game has three levels to choose from:')
    print(f'Easy: The code word will be {easy} characters long.')
    print(f'Medium: The code word will be {medium} characters long.')
    print(f'Hard: The code word will be {hard} characters long.')
    while True:
        level = input('What level would you like to play? ').lower()
        if level == 'easy':
            return easy
        elif level == 'medium':
            return medium
        elif level == 'hard':
            return hard
        else:
            print('I did not understand. Please enter one of "easy", "medium", or "hard".')

# this is where the computer selects a random code word
def computer_choose(level) -> str:
    char_list = ['A', 'B', 'C', 'D', 'E', 'F']
    code = ''
    while len(code) < level:
        code += random.choice(char_list) # random.choice(lst) picks one entry at random!
    #print(code)
    return code

# how the human picks a code -- it needs to check for:
#  -- length
#  -- that only the characters A - F are used
def human_guess(code): # we are only looking at code here so that they match in length!
    char_list = ['A', 'B', 'C', 'D', 'E', 'F']
    is_okay = False
    while not is_okay:
        guess = input(f'Please enter a guess of length {len(code)}.')
        if len(guess) != len(code):
            print('That is not the right length. Please try again.')
        else: # this is complicated -- we need to make sure they use correct characters
            is_okay = True
            i = 0
            while i < len(guess):
                if guess[i] not in char_list:
                    is_okay = False
                i += 1
            if not is_okay:
                print(f'Please only use characters in: {",".join(char_list)}')

    return guess

# how to make up the 'key' -- the sequence of XXo_ as appropriate
# there are a few difficulties here that make the code non-obvious
def make_key(code, guess) -> str:
    key = ''
    code_index = []
    guess_index = []

    # X's first (these are easy)
    i = 0
    while i < len(code):
        if code[i] == guess[i]:
            key += 'X'
            code_index.append(i)
            guess_index.append(i)
        i += 1

    # o's are harder -- we want to not over count!
    i = 0
    while i < len(code):
        j = 0
        while j < len(code):
            if guess[i] == code[j] and j not in code_index and i not in guess_index:
                key += 'o'
                code_index.append(j)
                guess_index.append(i)
            j +=1
        i += 1

    while len(key) != len(code):
        key += '_'

    return key


def print_status(guess_list,key_list):
    print('Guess', 'Keys')
    i = 0
    while i < len(guess_list):
        print(guess_list[i], key_list[i])
        i += 1


def play_game(level: int):
    code = computer_choose(level)
    guess_list = []
    key_list = []

    game_over = False

    while not game_over:

        guess = human_guess(code)
        key = make_key(code, guess)
        guess_list.append(guess)
        key_list.append(key)

        print_status(guess_list, key_list)

        if guess == code:
            game_over = True
            print(f'You win! It took you {len(guess_list)} steps.')
        elif len(guess_list) == 12:
            game_over = True
            print(f'You lose! The code was {code}.')
        else:
            print(f'You have {12 - len(guess_list)} tries remaining.')


def play_again() -> bool:
    while True:
        again = input('Would you like to play again? ')
        if again.lower() == 'yes':
            return True
        elif again.lower() == 'no':
            print('Thank you for playing Code Breaker!')
            return False
        else:
            print('Please answer "yes" or "no".')


def main():
    print_rules()

    again = True
    while again:
        level = set_level()
        play_game(level)
        again = play_again()

main()
