## Objects

# An object packages multiple pieces of data into a single item.
#   - The pieces of data stored in an object are called *fields*.
#   - Fields are "things an object knows".
# An object can also have functions which operate on the data in the object.
#   - The functions that an object can do are called *methods*.
#   - Methods are "things an object can do".

# Examples:
#   - Strings  (contain sequence of characters, have methods like .lower(), .split(), ...)
#   - Lists   (contains sequence of items, length..., methods like .append, ....)
#   - Dictionaries

## Classes

# Classes allow us to design our own new types of objects.
# A class is like a *blueprint* or *template* for objects.
#   e.g. a Car class tells us what all cars have in common, each individual car is an object.
#
# An object is an "instance of" a class.

from dataclasses import dataclass
import random

@dataclass
class Cake:   # social convention: use uppercase letters for class names
    # Write fields here with their types
    num_candles: int

    # Write methods here, inside the class.

    # Blow out a random number of candles
    def blow_out(self):
        r = random.randint(1, self.num_candles)
        self.num_candles -= r

    def all_out(self) -> bool:
        return self.num_candles == 0

# Name of the class used as a function is the way to create a new object of the class.
# e.g.   my_cake = Cake(50)    # creates a new Cake object with num_candles = 50.

# Take a cake, keep blowing out candles until they are all out, return # of steps it took.
def happy_birthday(c: Cake) -> int:
    count = 0
    while not c.all_out():
        c.blow_out()
        count += 1

    return count

def average_steps(num_candles: int, num_cakes: int) -> float:
    total: int = 0
    for _ in range(num_cakes):
        c: Cake = Cake(num_candles)
        total += happy_birthday(c)

    return total / num_cakes