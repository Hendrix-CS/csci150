# We can package up data and functions into "objects".
# Objects have:
#   - Data, i.e. things that they "know",
#   - Functions ("methods"), i.e. things that they "can do".
#
# e.g. string objects contain a sequence of characters,
#   and can do things like .lower(), .find(), ....

# Python "classes" let us design our own new kinds of objects.
# A class is like a template or blueprint for objects.
# e.g. class = car, objects = my car, your car, ...

# Objects are "instances" of a class.

import random

class Cake:

    # __init__ is a special method
    # which is called when a new object
    # is created.
    #
    # e.g.  cake = Cake()
    #
    # actually calls __init__.
    def __init__(self, num_candles: int):
        # self is a special parameter
        # that gets automatically filled in
        # by Python.  It contains a
        # reference to the object being created.

        self.candles = num_candles

    # Blow out a random number of candles from 1 .. n
    def blowout(self):
        n = random.randint(1, self.candles)
        self.candles -= n

    # Report whether the candles are all out or not.
    def allout(self) -> bool:
        return self.candles == 0

# Making Cake objects + references:
#
# >>> cake = Cake()   # make a new Cake object
# >>> cake.num_candles = 6
# >>> cake2 = cake
# >>> cake2.num_candles
# 6

# Keep blowing out candles until they are all out,
# return a count of the number of blows needed.
def happy_birthday(cake: Cake) -> int:
    count = 0
    while not cake.allout():
        cake.blowout()
        count += 1
    return count

# Make num_trials cakes with num_candles candles each
# and compute the average number of blows needed to
# blow out all the candles.
def average_blows(num_candles: int, num_trials: int) -> float:
    total = 0
    for i in range(num_trials):
        total += happy_birthday(Cake(num_candles))
    return total / num_trials

def generate_table():
    f = open("candle_data.txt", "w")
    for i in range(1,10001):
        avg = average_blows(100*i, 1000)
        f.write(str(100*i) + " " + str(avg) + "\n")
    f.close()