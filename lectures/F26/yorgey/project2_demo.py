# Top-down decomposition

def print_instructions():
    print("Instructions!")   # TODO

def play_game():
    print("Play the game.")

def ask_to_play_again() -> bool:
    return True   # TODO

def main():
    print_instructions()
    wants_to_play = True
    while wants_to_play:
        play_game()
        wants_to_play = ask_to_play_again()

main()