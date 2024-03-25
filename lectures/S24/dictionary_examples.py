from typing import *


def letter_count(s: str) -> Dict[str,int]:
    d = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        d[letter] = 0
    for letter in s:
        if letter.isalpha():
            d[letter.lower()] += 1
    return d


def sales_count(filename: str) -> Dict[str, int]:
    with open(filename) as f:
        counts = {}
        for line in f:
            item, price, count = line.split(',')
            count = int(count)
            if item not in counts:
                counts[item] = count
            else:
                counts[item] += count
        return counts


def revenue(filename: str) -> Dict[str, int]:
    with open(filename) as f:
        total_income_for = {}
        for line in f:
            item, price, count = line.split(',')
            revenue_for = int(price) * int(count)
            if item not in total_income_for:
                total_income_for[item] = revenue_for
            else:
                total_income_for[item] += revenue_for
        return total_income_for


def biggest_moneymaker(money_made: Dict[str,int]) -> str:
    best = None
    for key in money_made:
        if best is None or money_made[key] > money_made[best]:
            best = key
    return best


game_map = {
    'entrance': ['yard', 'living room'],
    'yard': ['entrance'],
    'living room': ['dining room', 'kitchen'],
    'kitchen': ['living room', 'backyard', 'dining room'],
    'backyard': ['kitchen'],
    'dining room': ['living room', 'kitchen']
}


def mapped_game(filename: str):
    my_map = build_map(filename)
    location = 'yard'
    command = ''
    while command != 'quit':
        print(f'You are at the {location}.')
        print(f'From here, you can move to {my_map[location]}.')
        command = input("Enter a move (quit to exit)")
        if command in my_map[location]:
            location = command


def build_map(filename: str) -> Dict[str,List[str]]:
    with open(filename) as f:
        map = {}
        for line in f:
            locations = line.strip().split(',')
            map[locations[0]] = locations[1:]
        return map