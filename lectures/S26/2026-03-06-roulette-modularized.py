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

    i = 0
    lst = options()

    while i < len(lst):
        print(f'{i+1}. {lst[i]}')
        i += 1

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
            i = 0
            lst = options()

            while i < len(lst):
                print(f'{i + 1}. {lst[i]}')
                i += 1


    return choice

def ball_roll() -> int:
    roll = random.randint(0,37)
    roll_str = str(roll)
    if roll == 37:
        roll_str = '00'
    print(f'The number {roll_str} was rolled.')

    return roll

def place_bet(stake) -> int:
    succ = False
    while not succ:
        bet = input(f'Your stake is ${stake}. How much do you want to bet? ')
        if bet.isdigit() and 1 <= int(bet) <= stake:
            succ = True
            bet = int(bet)
            return bet
        else:
            print(f"Please bet in whole dollar amounts, between 1 and {stake}.")

def even_odd(choice, roll, bet) -> int:
    if choice == 1 and roll % 2 == 0:
        return bet
    elif choice == 2 and roll % 2 != 0 and roll != 37:
        return bet
    else:
        return -bet

def thirds(choice, roll, bet) -> int:
    if choice == 3 and 1 <= roll <= 12:
        return 2 * bet
    elif choice == 4 and 13 <= roll <= 24:
        return 2 * bet
    elif choice == 5 and 25 <= roll <= 36:
        return 2 * bet
    else:
        return -bet



def main():
    welcome()
    print_rules()
    stake = 100

    cont = True
    while cont:

        choice = choose_bet(stake)

        if stake == 0:
            cont = False
            print(f'Thanks for playing. You finish with a stake of ${stake}.')
        elif choice == 6:
            cont = False
            print(f'Thanks for playing. You finish with a stake of ${stake}.')
        else:
            bet = place_bet(stake)
            roll = ball_roll()
            if choice == 1 or choice == 2:
                stake += even_odd(choice, roll, bet)
            elif choice == 3 or choice == 4 or choice == 5:
                stake += thirds(choice, roll, bet)




