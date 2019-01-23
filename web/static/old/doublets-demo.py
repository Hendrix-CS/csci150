###############################3
# Project 2 demo
# March 2018
# copyright 2018 Brent Yorgey
###############################3

# Repeatedly prompts the user for a valid English starting word
# Output: a valid English word
def pick_starting_word() -> str:
    print("Prompt the user for a starting word...")
    return "DOG"

# Repeatedly prompts the user for a valid English word
# which is the same length as the given starting_word
# Output: a valid English word.
def pick_ending_word(starting_word: str) -> str:
    print("Prompt for an ending word the same length as " + starting_word)
    return "CAT"

# Plays the doublets game, prompting user to get from starting_word to ending_word
def play_game(starting_word: str, ending_word: str):
    print("Fun game times")

# Asks the user if they want to play again.
# Output: True if they want to stop, False if they want to play again.
def wants_to_stop() -> bool:
    return False

def main():
    done = False

    while not done:
        # get the user to pick starting word
        starting_word = pick_starting_word()

        # get user to pick an ending word
        ending_word = pick_ending_word(starting_word)

        # play the game
        play_game(starting_word, ending_word)

        done = wants_to_stop()

main()