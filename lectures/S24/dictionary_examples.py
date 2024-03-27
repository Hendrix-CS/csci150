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


def bartender():
    tabs = {}
    command = ""
    while command != 'quit':
        print("1: Input a transaction")
        print("2: Check out")
        print("3: List all tabs")
        command = input("Enter number or 'quit' to exit")
        if command == '1':
            record_tab(tabs)
        elif command == '2':
            check_out(tabs)
        elif command == '3':
            display_tabs(tabs)


def record_tab(tabs: Dict[str,int]):
    customer = input("Enter name: ")
    cost = int(input("Cost of drink, in cents: "))
    if customer in tabs:
        tabs[customer] += cost
    else:
        tabs[customer] = cost


def check_out(tabs: Dict[str,int]):
    customer = input("Enter name: ")
    if customer in tabs:
        print(f"{customer} owes {tabs[customer]} cents.")
        money = int(input(f"How much money did {customer} pay? "))
        if money < tabs[customer]:
            tabs[customer] -= money
            print(f"{customer} still owes {tabs[customer]} cents.")
        else:
            change = money - tabs[customer]
            tabs.pop(customer)
            if change == 0:
                print(f"{customer} has settled up exactly.")
            else:
                print(f"Hand {customer} {change} cents back.")
    else:
        print(f"{customer} does not have a tab")


def display_tabs(tabs: Dict[str, int]):
    for customer in tabs:
        print(f"{customer}: {tabs[customer]}")