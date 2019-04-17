import random

# We've seen complex objects in Python such as lists, strings, dictionaries, files...
# These objects have two things:
#   1. Some kind of data
#   2. Functions you can use

# Using classes we can make our own.

# A 'class' is like a blueprint for objects.
# It describes 1. what data the objects will store, 2. what functions they have.

# Let's make a Cake class to represent cakes with candles.

class Cake:     # Typically class names start with uppercase

    # This is a special function called a 'constructor'
    # that says how to make a new Cake object.
    #
    # __init__ is a special name that Python looks for
    # self will be a reference to the object being created
    #   it will be filled in automatically by Python.
    #
    # When we write something like  Cake(6)  Python automatically
    # turns it into  __init__(self, 6)
    def __init__(self, init_candles: int):
        self.candles = init_candles

    # Pick a random number of candles to blow out
    def blow_out_candles(self):
        n: int = random.randint(1, self.candles)
        self.candles -= n

    # Return true if the number of remaining candles is 0,
    # or False otherwise.
    def allout(self) -> bool:
        # if self.candles == 0:
        #     return True
        # else:
        #     return False

        # b: bool = False
        # if self.candles == 0:
        #     b = True
        # return b

        # Much shorter!
        return self.candles == 0

    # Repeatedly blow out a random number of candles until they are all out,
    # and report how many times it took.
    def blow_out_all_candles(self) -> int:
        count: int = 0
        while not self.allout():
            self.blow_out_candles()
            count += 1
        return count


def blows_for_candles(candles: int) -> float:
    sum: int = 0
    for _ in range(1000):
        cake = Cake(candles)
        sum += cake.blow_out_all_candles()
    return sum / 1000

for c in range(100):
    print(str(c) + " " + str(blows_for_candles(100*c)))