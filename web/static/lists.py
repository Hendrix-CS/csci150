# Lists!

# A list is a sequence of (any) values, with indices 0, 1, 2, ...

# Can do a lot of the same things on lists as on strings:
#   indexing [i]
#   slices
#   len(...)
#   +
#   *

from typing import *

animals: List[str] = ['echidna', 'giraffe', 'leopard', 'skua', 'marmot', 'penguin', 'rhinoceros', 'seal', 'stegosaurus', 'turtle']


# Print all the strings in 'items', each on a separate line
def explode_list(items: List[str]):
    n: int = 0
    while n < len(items):
        print(items[n])
        n += 1

# Repeatedly prompt the user for input until they type 'quit',
# then return a list of all the user's inputs (excluding 'quit').
def read_inputs() -> List[str]:
    done = False
    x=[]
    while not done:
        y=input('Please enter something: ')
        if y=='quit':
            done = True
        else:
            x.append(y)

    return x