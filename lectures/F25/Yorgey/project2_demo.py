def print_rules():
    print('Rules!')


def play_game(difficulty: int):
    print(f'Playing game with difficulty {difficulty}!')


def ask_play_again() -> bool:
    return False


def ask_difficulty() -> int:
    # TODO: loop until they enter something valid
    d = int(input('What difficulty would you like?'))
    return d


def main():
    print_rules()
    wants_to_play = True
    while wants_to_play:
        difficulty = ask_difficulty()
        play_game(difficulty)
        wants_to_play = ask_play_again()

main()