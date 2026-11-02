# Reminders:
#   Quiz this Friday, Dictionaries
#   Final Project Design Document Due Monday, November 16 (2 weeks)
#  Homework Due Today, Dictionaries

# Today, we introduce the last "big" topics in class
# (don't worry, we'll do other things).
# Classes and objects
#
# Consider simple store:
#
# A cash register has a lot of properties we might be interested in
#   how much money is currently in the "til"
#   how many transactions have been processed
#   what items have been purchased at that register

# In fact, each inventory item could also be a 'thing': Each item has
#  * name, likely a string
#  * unit price, a float
# * number in stock, an integer
#
# While we could use a list, we really shouldn't -- lists should be homogenous
# and we could also mess up by appending/poping

# We can encapsulate this information in a single "thing" in memory
# We call such an encapsulation a(n):
#   "object," when talking about individual instances
#   "class," for the overarching type of object
#
# the 'variables' that an object has are called its "attributes"
# syntactically: if obj is a particular obj and first_name is one of its attributes, we write
# obj.first_name to access it

# a function which "belongs" to a class is called a "method," rather than a function.
# I will try very hard to use the right term each time; we have seen this before:

#len(s) is a function, basically because "length" does not belong only to strings
# -- also to lists and any other iterable type object
# other functions -- like all of the fun1(), aaa()
# are functions since they are not specific to any class

# s.lower()  -- lower() is a string method
# lst.append(7) -- append() is a list method

#Bascially, it is a function if its syntax is "mathematical" -- i.e. fun(object)
# it is a method when it used the "dot" version:  object.method()

# This distinction matters, but really only at a level beyond CSCI 150
# It is subtle, and there are not quiz questions about the difference


# A very simple, toy example:
# we will have 2 attributes -- a value (called 'val') and name

from dataclasses import dataclass

@dataclass
class Toy:

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




## Another Example
# A 'Player' class, which represents a character in a text-based adventure game
#
# Each Player will have:
# -- a name
# -- health points
# -- damage -- the maximum number of damage they do to others in an attack
# -- alive: a boolean

# Methods:
# -- heal() -- will increase health points by 3 units
# -- attack(other) -- will do random damage to other player
# -- get_status() -- will print a message with info about the player


import random
@dataclass
class Player:


    name: str
    health_points: int
    damage: int
    alive: bool = True

    def heal(self):
        if self.alive:
            self.health_points += 3
        else:
            print(f'{self.name} is dead and cannot be healed.')


    def attack(self, other):
        if not self.alive:
            print(f'{self.name} is dead and cannot attack.')

        elif not other.alive:
            print(f'{other.name} is already dead. You cannot attack them.')

        else:
            dam = random.randint(1,self.damage)
            other.health_points -= dam

            print(f'{self.name} does {dam} damage to {other.name}.')

            if other.health_points <= 0:
                other.alive = False
                print(f'{other.name} has been killed.')

    def get_status(self):
        if self.alive:
            alive_str = 'alive'
        else:
            alive_str = 'dead'
        print(f'{self.name} has {self.health_points} and is currently {alive_str}.')

