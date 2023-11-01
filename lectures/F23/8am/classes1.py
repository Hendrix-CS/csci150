# *Objects* give us a way to "package up" (1) multiple pieces of information
# together with (2) some functions ("methods") that operate on the information.

# e.g. lists:
#   - (1) lists store a sequence of elements, keeps track of length, etc.
#   - (2) can do various functions (methods) like .append(), len(...), .sort(), ...
#
# e.g. strings
#
# e.g. files (what is returned from the open function)
#   - (1) stores name of the file, where we are in the file, etc.
#   - (2) gives us methods like .readlines(), .read(), .close(), ....

# *Classes* are like blueprints for objects.  A class says what a bunch of objects
# are all going to be like.

from cake import *

# Create a cake with a certain number of candles and report how many
# blows are needed to blow out all the candles.
def happy_birthday(num_candles: int) -> int:
    cake: Cake = Cake(num_candles)
    while not cake.all_out():
        cake.blow_out()
    return cake.get_num_blows()

# Run 1000 experiments with the given number of candles, return
# average number of blows needed.
def average_blows(num_candles: int) -> float:
    total: int = 0
    for _ in range(1000):
        total += happy_birthday(num_candles)

    return total / 1000

def main():
    for n in range(1000):
        print(f'{n*100} {average_blows(n*100)}')

main()