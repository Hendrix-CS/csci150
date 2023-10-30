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

import random

class Cake:    # class names starting with uppercase is standard style

    # '__init__' is a special name that will be used every time
    # we create a new object of this class.
    # e.g. it is called automatically every time we say Cake().
    #
    # 'self' is a special reference to the object being created.
    # It is always filled in automatically by Python; we never
    # have to give it as a parameter.
    def __init__(self, candles: int):
        # Create a 'num_candles' variable inside the
        # object being created.
        self.num_candles = candles

    # Method to blow out a random number of candles.
    # self will always be the first parameter to any method defined inside a class.
    def blow_out(self):
        c: int = random.randint(1, self.num_candles)
        self.num_candles -= c

    def all_out(self) -> bool:
        return self.num_candles == 0

        # if self.num_candles == 0:
        #     return True
        # else:
        #     return False

# To create a new object of this class:
# cake: Cake = Cake()
# "variable cake has type Cake, and is equal to a new Cake object"