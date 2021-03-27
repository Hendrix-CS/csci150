from typing import *
import random

# Guess the word!

def main():
    print_instructions()
    play_game()

def print_instructions():
    print("Welcome to the Guess The Word game!")
    print("I will pick a word and you try to guess it.")


def choose_difficulty() -> str:
    print("Choosing easy difficulty!")
    return 'hard'

def difficulty_len(difficulty: str) -> int:
    if difficulty == 'easy':
        return 5
    elif difficulty == 'medium':
        return 8
    elif difficulty == 'hard':
        return 12

def choose_random_word(difficulty: str) -> str:
    english_file = open('english3.txt', 'r')
    words: List[str] = english_file.readlines()
    word: str = random.choice(words).strip()
    while len(word) != difficulty_len(difficulty):
        word: str = random.choice(words).strip()
    return word


def user_guess(difficulty: str, word: str):
    print(f'Try to guess the word! Hint: it\'s {word}')


def play_one_game():
    # choose difficulty
    difficulty: str = choose_difficulty()
    # pick random word
    word: str = choose_random_word(difficulty)
    # let the user guess
    user_guess(difficulty, word)

def prompt_for_valid_input(prompt: str, valid_inputs: List[str]) -> str:
    valid: bool = False
    response: str = ''
    while not valid:
        response = input(prompt)
        if response.lower() in valid_inputs:
            valid = True
        else:
            print("That was not valid, try again.")

    return response.lower()


def ask_user_if_play_again() -> bool:
    return prompt_for_valid_input("Do you want to play again? (y/n) ", ['y', 'n']) == 'y'


def play_game():
    play_again: bool = True
    while play_again:
        play_one_game()
        play_again = ask_user_if_play_again()


main()