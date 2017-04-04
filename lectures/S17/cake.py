import random

# Birthday cake problem

# If there are n lit candles, blow out a random number
# between 1 and n
# How many rounds does it take (on average) before
# all the candles are out?

# We can package up data and functionality into "objects"
# Objects have "information they know" (variables)
# Objects have "things they can do" (functions)

# For example, strings:
#   They contain some information (list of characters)
#   They have things they can do (e.g. .lower(), .find(), .count(), ...)

# Python classes let us design our own objects.
# Classes are like templates/blueprints for objects.

# e.g. class = "car", objects = "my car", "your car", ...

class Cake:
    ### Stuff a Cake object knows/remembers:
    
    # Every Cake object will have an int variable
    # called num_lit_candles.

    # (Python does not require us to say this, so we put it
    # in a comment.)

    ### Stuff a Cake object can do:

    # How to create a new Cake object:

    # __init__ is a special method that gets called when we
    #   create a new Cake object.
    # self is a special first parameter that gets filled in by
    #   Python, which refers to the object being created.
    # num_candles is the information we need to specify when
    #   creating a Cake.
    def __init__(self, num_candles):

        self.num_lit_candles = num_candles

    # Input: number of candles to blow out
    # Blows out that many candles (assuming num_candles is
    #   <= num_lit_candles)
    def blowout(self, num_candles):
        self.num_lit_candles -= num_candles

    # Blow out a random number of candles from 1 to
    #   num_lit_candles.
    def blowout_random(self):
        n = random.randint(1, self.num_lit_candles)
        self.blowout(n)

    # Return true if all the candles are blown out.
    def allout(self):
        return self.num_lit_candles == 0


#############################

# Input: a Cake
# Keep blowing out a random number of candles
#   until they are all out, and report how many times
#   it took.
def happy_birthday(cake):
    count = 0
    while not cake.allout():
        cake.blowout_random()
        count += 1
    return count






