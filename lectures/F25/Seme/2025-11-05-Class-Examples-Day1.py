from dataclasses import dataclass
import random


# Classes Homework due on Monday
#
# Final Project Design Document due Friday, Nov 15


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



# An example, stolen from Dr. Yorgey -- with permission!
@dataclass
class Cake:   # social convention: use uppercase letters for class names
    # Write fields here with their types
    num_candles: int

    # Write methods here, inside the class.

    # Blow out a random number of candles
    def blow_out(self):
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
    for _ in range(num_cakes):
        c: Cake = Cake(num_candles)
        total += happy_birthday(c)

    return total / num_cakes





# A variation on the Player Game from earlier




# @dataclass
# class Weapon:
#     name: str
#     min_dam: int
#     max_dam: int
#
# @dataclass
# class Player1:
#
#     name: str
#     health: int
#     alive: bool = True
#
#
#
#     def attacks(self, other, weapon):
#         if not self.alive:
#             print('You are dead. Sorry!')
#         else:
#             if not other.alive:
#                 print(f"{other.name}'s already dead!")
#             else:
#                 damage = random.randint(weapon.min_dam, weapon.max_dam)
#                 other.health -= damage
#                 print(f'{self.name} does {damage} damage to {other.name} with an {weapon.name}.')
#                 if other.health <=0:
#                     print(f'{self.name} killed {other.name}.')
#                     other.alive = False
#
#
#
#     def status(self):
#         print(f'{self.name} has {self.health} health points.')
#         if not self.alive:
#             print(f'{self.name} is dead.' )









