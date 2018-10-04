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

# Add three gerbils to the end of animals

# This builds the correct list, but doesn't change animals
# animals + ['gerbil', 'gerbil', 'gerbil']

# Works
# animals += ['gerbil', 'gerbil', 'gerbil']

# Works
# animals.append('gerbil')
# animals.append('gerbil')
# animals.append('gerbil')

# Infinite loop
# while len(animals) < (len(animals) + 3):
    # do stuff

# Works
# num_animals: int = len(animals)
# while len(animals) < (num_animals + 3):
#     animals.append('gerbil')

# Works
# count: int = 0
# while count < 3:
#     animals.append('gerbil')
#     count += 1
#

# Works
# animals += ['gerbil'] * 3

# Not an error, but for a strange reason!
# animals += 'gerbil' * 3

# Doesn't work
# animals.append('gerbil' * 3)

# Also doesn't work
# animals.append(['gerbil'] * 3)

# Also also doesn't work
# animals.append(' '.join(['gerbil'] * 3))