from typing import *

# Reminders:
#   New Homework -- Classes, due on Monday next week
#   Final Project Design Document Due Friday, Nov 15



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
#  * name
#  * unit price
# * number in stock

# We can encapsulate this information in a single "thing" in memory
# We call such an encapsulation a:
#   "object," when talking about individual instances
#   "class," for the overarching type of object

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




#############################################################
# Let's look at some simpler examples before we implement it

# With a class, we can define out *own* new type of data
#  Your class defines a "blueprint" for each individual object
#
#  Car class might be defined, and objects would be my Honda Fit,
#  my wife's Honda CRV, or my older daughter's Accord
#  (notice a theme with our family....)

#  What things might we want to keep up with?

#    Milleage
#    Gas Tank (Capacity & current level)
#    lots of other things

#   A Car class would allow us to encapsulate all of these things
#   into a single piece of data

#    Any particular object -- that is any particular instance of a car
#    -- would have all of these attributes defined and usable

# #############
# Another Example
#  Books and Bookshelves
#  We might have a Book class -- title, author, page count, etc
#   and a Shelf class -- how many shelves, each shelf's capacity, which books are on which shelf.
#
#   In fact, we will implement Book & Shelves versions later.



class Car:
    # though not required, the style in Python is to Capitalize the name of the class

    def __init__(self, curr_gas: float, tank_cap: float, mpg: float):

        # __init__ is a special method
        #   that gets called when a
        #   new object is created.
        #   i.e. when Car() is called.
        # __init__  is two underscores, init, two underscores

        # 'self' is a special variable, which allows Python to refer back to the individual object

        # list of attributes -- things any car "knows" about itself
        self.gas = curr_gas
        self.tank_cap = tank_cap
        self.mpg = mpg
        self.milleage = 0

    ## two special methods follow -- I'll talk about them in a bit

    def __repr__(self):
        return f'Car({self.gas},{self.tank_cap},{self.mpg})'

    def __str__(self):
        return f'A car with {self.gas} gallons in a {self.tank_cap} tank. The car has {self.milleage} miles and gets {self.mpg} MPG'


    def fill(self, gas: float):
        self.gas += gas

        if self.gas > self.tank_cap:
            self.gas = self.tank_cap

    def drive(self, dist: float):
        max_dist = self.gas * self.mpg

        if dist > max_dist:
            print('You do not have enough gas to go that far!!')
        elif dist <= 0:
            print('You must travel a positive distance.')
        else:
            self.gas = self.gas - dist / self.mpg
            self.milleage += dist

    # # this method is nice, but basically is replaced with __str__ and __repr__ above.
    def status(self):
        print(f'It currently has {self.gas} gallons in the tank, which holds {self.tank_cap} gallons.')
        print(f'The car has {self.milleage} miles on it.')
    #








class Student:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.courses = []
        self.credits = 0
        self.year = 'freshman'

    def add_course(self, course: str):
        self.courses.append(course)
        self.credits += 1

    def drop_course(self, course: str):
        if course not in self.courses:
            print(f'That course is not on {self.name}s schedule.')
        else:
            self.courses.remove(course)
            self.credits -= 1















# class Student:
#
#     def __init__(self, name: str, id: int):
#         self.name = name
#         self.id = id
#         self.yr = 'Freshman'
#         self.credits = 0
#         self.schedule = []
#
#     def add_course(self,course: str):
#         self.schedule.append(course)
#         self.credits += 1
#
#     def drop_course(self, course: str):
#         if course in self.schedule:
#             self.schedule.remove(course)
#         else:
#             print(f'{} is not enrolled in {course}')
#
#     def is_full_time(self) -> bool:
#         if self.credits >= 3:
#             return True
#         else:
#             return False
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
