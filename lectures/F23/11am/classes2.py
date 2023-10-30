# Objects:
#   - store (possibly multiple) pieces of information (things they "know")
#   - have functions ("methods") that operate on that information
#     (things they can "do")
#
# Examples:
#   - lists
#   - strings
#   - file objects
#     - stores information like name of file, position in the file, etc.
#     - provides functions like .readlines(), .close(), ....

import random

# A "class" is like a blueprint for objects.  Defines what variables + functions they will have.
# Each object is an "instance" of a class.  e.g. specific cars are instances of the "car" class.

# Common Python style is to use capital letters for names of classes.
class Cake:

    # def inside a class creates a "method", i.e. a function that objects of the class
    # will be able to do.

    # __init__ is a special method name: Python will use it automatically every time
    # we create an object of this class.
    #
    # self is a special parameter which is a reference to the object being created,
    # or the object which is being asked to run the function.  It is required
    # for every class method, but it is automatically filled in by Python.
    def __init__(self, candles: int):
        self.num_candles = candles
        self.num_blows = 0

    # Tell a cake to blow out a random number of candles.
    def blow_out(self):
        c: int = random.randint(1, self.num_candles)
        self.num_candles -= c
        self.num_blows += 1

# my_cake: Cake = Cake()  # Create a new Cake object and put it in my_cake,
#   which is a variable that will store references to Cake objects

# A "dot" as in  my_cake.num_candles  means
# "follow the reference/arrow to the other end".