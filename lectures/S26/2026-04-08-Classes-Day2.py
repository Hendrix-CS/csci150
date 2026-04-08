# Reminders:
#   Quiz this Friday, Dictionaries
#   Final Project Design Document Due Friday, April 17

from dataclasses import dataclass
import random

# From last time:
class Toy:

    def __init__(self, x: int, s: str):
        self.val = x
        self.name = s

    # __init__ is a special method
    #   that gets called when a
    #   new object is created.
    # it should contain all of the attributes you want to use
    # __init__  is two underscores, init, two underscores

    # 'self' is a special variable, which allows Python to refer back to the individual object

    def print_name(self):
        print(self.name)

    def add_val(self,x: int):
        self.val += x

    def print_val(self):
        print(self.val)

    def get_val(self):
        return self.val


# Easier (??) way:

@dataclass
class Toy1:
    val: int
    name: str

    def print_name(self):
        print(self.name)

    def add_val(self,x: int):
        self.val += x

    def print_val(self):
        print(self.val)

    def get_val(self):
        return self.val



# Interacting class objects
# A very simple game -- multiple players which can attack each other
@dataclass
class Player:

    name: str
    health: int
    alive: bool = True



    def attacks(self, other):
        if not self.alive:
            print('You are dead. Sorry!')
        else:
            if not other.alive:
                print(f"{other.name}'s already dead!")
            else:
                damage = random.randint(1,4)
                other.health -= damage
                print(f'{self.name} does {damage} damage to {other.name}.')
                if other.health <=0:
                    print(f'{self.name} killed {other.name}.')
                    other.alive = False



    def status(self):
        print(f'{self.name} has {self.health} health points.')
        if not self.alive:
            print(f'{self.name} is dead.' )

############
# Data Classes work well when you do not have complicated default values
# when the class is initialized.
# If you need an attribute in a class to be a list or a dictionary or
# some complicated structure a 'regular' class (like the first Toy above)
# is likely the best option.

# An example, stolen from Dr. Yorgey -- with permission!
@dataclass
class Cake:

    num_candles: int


    def blow_out(self):
        if self.all_out():
            print('The cake is out of candles.')
        else:

            r = random.randint(1, self.num_candles)
            self.num_candles -= r

    def all_out(self) -> bool:
        return self.num_candles == 0

# Name of the class used as a function is the way to create a new object of the class.
# e.g.   my_cake = Cake(50)    # creates a new Cake object with num_candles = 50.

# Take a cake, keep blowing out candles until they are all out, return # of steps it took.
def happy_birthday(c: Cake) -> int:
    count = 0
    while not c.all_out():
        c.blow_out()
        count += 1

    return count

def average_steps(num_candles: int, num_cakes: int) -> float:
    total: int = 0
    for n in range(num_cakes):
        c: Cake = Cake(num_candles)
        total += happy_birthday(c)

    return total / num_cakes


def ave_to_n(n: int):
    f = open('candles.txt','w')
    for i in range(1, n + 1):
        f.write(f'{i};{average_steps(i,1000)}\n')

    f.close()

