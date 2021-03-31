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

    # Number of times we have blown out some candles
    num_blows: int

    # Pick a random number of candles and blow them out.
    def blowout(self):
        r = random.randint(1, self.num_candles)
        self.num_candles -= r
        self.num_blows += 1

    # Ask whether all the candles are out.
    def all_out(self) -> bool:
        return self.num_candles == 0

    def get_num_blows(self) -> int:
        return self.num_blows

# Keep blowing out candles on the cake c until all out,
# and return the number of blows required.
def happy_birthday(c: Cake) -> int:
    while not c.all_out():
        c.blowout()
    return c.get_num_blows()


def average_blows(num_candles: int, num_cakes: int) -> float:
    total: int = 0
    for i in range(num_cakes):
        c: Cake = Cake(num_candles, 0)
        total += happy_birthday(c)

    return total / num_cakes

def main():
    for num_candles in range(500):
        avg: float = average_blows(num_candles, 1000)
        print(f'{num_candles} {avg}')

main()