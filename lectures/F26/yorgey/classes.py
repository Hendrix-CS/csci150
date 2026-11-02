# Classes & objects!

# Objects:
# Objects give us a way to package up some data + some operations on that data.
#   - Objects can contain some variables (*fields*), i.e. "things the object knows/remembers".
#   - Objects can also have functions (*methods*), i.e. "things the object can do".

# We have already seen objects:
#   - lists
#     - has some fields that keep track of items, length, etc.
#     - has methods such as  .append(), .pop(), ...
#   - strings
#     - fields: sequence of characters
#     - methods: .upper(), .lower(), .strip()
#
# dot is how we access fields/methods of an object

# Classes:
# A *class* allows us to design our own new types of objects.
#
# A class is like a *template* or *blueprint* for objects.
# Each individual object is an "instance of" a class.


# Let's make a class to represent birthday cakes.

from dataclasses import dataclass
import random

@dataclass
class Cake:    # class names start w/ uppercase letter by convention (Python does not care, but humans do)
    # fields, i.e. things every Cake object will know/remember

    num_candles: int

    # methods, i.e. things every Cake object can do.
    # A method is just a function 'def' *inside* a class.
    # Every method has a special first parameter called 'self' which
    # refers to the object that the method is called on.
    def blow_out(self):

        # To refer to fields in the object (e.g. num_candles),
        # we can write  self.<field>  e.g.  self.num_candles
        n = random.randint(1, self.num_candles)

        # n is just a local variable defined in this function, so
        # we do not use 'self.' with n
        self.num_candles -= n

    def all_out(self) -> bool:
        return self.num_candles == 0

    def blow_all_out(self) -> int:
        count = 0
        while not self.all_out():
            self.blow_out()
            count += 1
        return count

# The name of the class is also a special function that creates a new object
# of that class.  e.g.  Cake(n) to create a new Cake object, where n is the intial
# value for num_candles.