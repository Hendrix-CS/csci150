import random

# We can package data and functionality into "objects".
# Objects have things they "know", i.e. variables
# and things they can "do", i.e. functions/methods.

# Python "classes" let us design our own new objects.
# Class is a template or blueprint for objects.
# An object is an "instance" of a class.

# e.g. class = Car,  object = my car.

class Cake:   # we usually capitalize the name of a class

    # __init__ is a special method that gets called
    # every time we make a new Cake object,
    # i.e. when Cake() is called.
    def __init__(self, num_candles):
        # self is a special parameter automatically filled in
        # by Python with a reference to the object being
        # created.
        # The rest of the parameters come from arguments
        # to  Cake(...)
        # e.g. when we call  Cake(10), it will turn into
        #  __init__(self, 10)

        # self.candles is a variable contained in the object
        # remember num_candles parameter in self.candles.
        self.candles = num_candles

    # Methods = things that all Cakes can do
    # Note all methods take 'self' as a special first parameter

    # Picks a random number of candles to blow out.
    def blowout(self):
        n = random.randint(1, self.candles)
        self.candles -= n

    # Output: true or false, if all candles are blown out
    def allout(self):
        return (self.candles == 0)

# Input: a Cake object
# Output: # of times it called blowout() before all the
#   candles were out.
def happy_birthday(c):
    count = 0
    while not c.allout():
        c.blowout()
        count += 1
    return count

def average_blows(num_candles, num_cakes):
    total = 0
    for i in range(num_cakes):
        c = Cake(num_candles)
        total += happy_birthday(c)
    return total / float(num_cakes)

def main():
    for num_candles in range(100):
        print num_candles, average_blows(num_candles, 10000)
