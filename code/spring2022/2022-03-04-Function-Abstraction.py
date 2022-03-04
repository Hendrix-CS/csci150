from typing import *

# Function Abstraction

# We have been writing a lot of small functions that do small tasks
#
# Though some of that is because this is an intro level course,
# it is also true that most programming takes place at the small function
# small individual task level

# Benefits:
# Easier to debug
# Easier to understand
# Often can reuse already-written code
# Easier to modify/update as needed

# Function Abstraction -- big picture: assume each small function
# works correctly. How do the pieces fit together? In fact *what* pieces are even needed?

# Modularity -- breaking complicated tasks into small, manageable chunks
# Very rarely should a function be more and 15 lines or so long (this is not a hard and fast rule)


#############################################
# Our task for today

# Start to build a simple store cash register


# User will tell us which item they'd like to purchase, and how many


# The register will find the total value of the sale, and keep up
# with the total 'cash on hand' and a list of all items sold


def sell_item() -> str:
    item = input('What would you like to purchase? ')
    return item

def update_sold(items_sold: List[str],item: str) -> List[str]:
    items_sold.append(item)
    return items_sold

def item_price() -> float:
    is_okay = False
    while not is_okay:
        price = input('Please enter the item price: ')
        if price[-3] == '.' and price[-2:].isdigit()  and price[:-3].isdigit():
            is_okay = True
        else:
            print('That is not a valid price.')

    return float(price)


def main():
    items_sold = []
    cash = 100
    cont = True
    while cont:
        choice = input('What would you like to do? ')
        if choice == 'sell':
            item = sell_item()
            items_sold = update_sold(items_sold,item)

        elif choice == 'cash':
            print(cash)

        elif choice == 'list':
            print(','.join(items_sold))

        elif choice == 'exit':
            cont = False

        else:
            print('Please enter a valid response.')
    # have options
    # sell an item
    # check list of items sold
    # check cash on hand
    # others












    



