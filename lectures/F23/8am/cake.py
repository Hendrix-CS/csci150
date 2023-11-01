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
        self.num_blows = 0

    # Method to blow out a random number of candles.
    # self will always be the first parameter to any method defined inside a class.
    def blow_out(self):
        c: int = random.randint(1, self.num_candles)
        self.num_candles -= c
        self.num_blows += 1

    def all_out(self) -> bool:
        return self.num_candles == 0

        # if self.num_candles == 0:
        #     return True
        # else:
        #     return False

    def get_num_blows(self) -> int:
        return self.num_blows

# To create a new object of this class:
# cake: Cake = Cake()
# "variable cake has type Cake, and is equal to a new Cake object"
