import random

def welcome():
    print("Welcome to Roulette, the simplest Casino Table Game!")
    print()
    print("You will start with a stake of $100.")
    print("You can place any size bet -- whole dollar amounts -- up to your stake.")
    print("There are 38 possible slots -- the numbers 1 - 36, and 0, and 00.")
    print()
    print("Note that 0 and 00 are not considered even!")

def print_rules():
    print("You can bet on any of the following:")
    print()
    print("1. Evens (pays 1:1)")
    print("2. Odds (pays 1:1)")
    print("3. 1st 12 (pays 2:1)")
    print("4. 2nd 12 (pays 2:1)")
    print("5. 3rd 12 (pays 2:1)")
    print("6. Quit")
    print()
    print()
    input('Press "Enter" to start')

def options() -> list[str]:
    lst = []
    lst.append("Evens (pays 1:1)")
    lst.append("Odds (pays 1:1)")
    lst.append("1st 12 (pays 2:1)")
    lst.append("2nd 12 (pays 2:1)")
    lst.append("3rd 12 (pays 2:1)")
    lst.append("Quit")

    return lst
def choose_bet(stake: int) -> int:
    print(f'Your current stake is ${stake}.')
    succ = False
    while not succ:
        choice = input('What type of bet would you like to make? (1-6): ')
        if choice.isdigit() and 1 <= int(choice) <= 6:
            succ = True
            choice = int(choice)
        else:
            print("You can bet on any of the following:")
            print("1. Evens (pays 1:1)")
            print("2. Odds (pays 1:1)")
            print("3. 1st 12 (pays 2:1)")
            print("4. 2nd 12 (pays 2:1)")
            print("5. 3rd 12 (pays 2:1)")
            print("6. Quit")

    return choice


def main():
    welcome()
    print_rules()
    stake = 100

    cont = True
    while cont:



        if stake == 0:
            cont = False
        # elif choice == 6:
        #     cont = False

