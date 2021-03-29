# We can package up data into *objects*.
# - Objects contain some variables, i.e.
#   things the objects remember.
# - Objects also have functions, i.e.
#   things they can do.

# Python *classes* allow us to design our own new kinds of
# objects.
# - A class is a *template* or a *blueprint* for objects.
# - An object is an "instance of" a class.
#   e.g. we could have a class for cars, and each
#   actual, individual car would be like an object.

from dataclasses import dataclass
import random

# @dataclass is a magic incantation we will put
# before every class
@dataclass
class Cake:    # names of classes traditionally start
               # with a capital letter

    # Every Cake object will have a variable called
    # num_candles, which is the number of candles
    # currently lit
    num_candles: int

    # Pick a random number of candles and blow them out.
    def blowout(self):
        r = random.randint(1, self.num_candles)
        self.num_candles -= r


def main():
    my_cake: Cake = Cake(100)
    while my_cake.num_candles > 0:
        my_cake.blowout()

main()