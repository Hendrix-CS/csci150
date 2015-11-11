# 4 November 2015
# Introduction to classes & objects

# We can package up data into "objects"
# Objects have functions, i.e. things they
#   can do. aka "Methods".

# Python "classes" allow us to design our
#   own new kinds of objects.

# Birthday cake problem:
  # If n lit candles, blow out a random # between
  #   1 and n
  # How many blows does it take (on average)
  #   before they are all out?

import random

# class = template for objects
# an object is an "instance of" a class
# e.g. class = Car, object = my car
class Cake:

    # __init__ is a special method
    #   that gets called when a
    #   new object is created.
    #   i.e. when Cake() is called.
    def __init__(self, num_candles):
        # self is a special first parameter
        # that gets filled in by Python

        # self.candles is a variable in the
        #   object being created
        #   (candles = ... would make a local var)
        self.candles = num_candles

    # Methods = things that all Cakes can do

    def blowout(self):
        n = random.randint(1, self.candles)
        self.candles -= n

    def allout(self):
        return (self.candles == 0)


def one_cake(c):
    count = 0
    while not c.allout():
        c.blowout()
        count += 1

    return count

def average(num_candles, trials):
    total = 0
    for i in range(trials):
        c = Cake(num_candles)
        total += one_cake(c)
    return total / float(trials)

def main():
    for num_candles in range(100):
        print num_candles, average(num_candles, 10000)

main()
