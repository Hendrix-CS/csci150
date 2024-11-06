from typing import *

# Classes Homework due on Monday
#
# Final Project Design Document due Friday, Nov 15



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


class Course:
    1





############################################
# Fountain Example
############################################
# We want to write a class called Fountain.
# Objects in this class have three attributes:
#   *  their capacity (in liters)
#   *  the amount of water (also in liters) currently in the fountain
#   *  whether the fountain is currently running or not

# Initially, fountains start out empty, off, and with a parameter capacity
#
# So, that a = Fountain(100) would create a Fountain object which is
#  empty, off, and can contain at most 100 liters

# Besides __init__ we want to add three methods:
#     add(liters: int) which will add liters amount of water:
#          if adding brings the total above capacity, the excess will overflow, and
#               the fountain will contain its capacity
#           if liters is negative, add will actually subtract water from the fountain
#           the total contents cannot become negative -- if you remove "too much"
#           the amount should be set to 0
#           if the amount is ever 0, the fountain should be turned off
#
#   toggle() - will change the fountain from on to off, or off to on, except
#       if the fountain is off and empty, toggle will not turn it on. Instead
#       a message to the user should be printed
#
#   look()  - prints (not returns) a string which describes the state of the fountain.

class Fountain:

    1



############
# Player class --
# Imagine that we have a group of people who all play head-to-head games
# Each player will have 3 attributes:
#  name -- a string
#  wins -- number of wins (an int)
#  loses -- number of loses (also an in)

# We will have one method, beats(), which wil be formatted as
#   a.beat(b) to mean that player a has defeated player b
#
#
class Player:
    1




## We could expand this to have each player with a win_list and loss_list,
# which would add the other player to the appropriate list





#### Sample Code
# class Fountain:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.amount = 0
#         self.on = False
#
#
#
#
#
#
#
#     def __repr__(self):
#         return f'Fountain({self.capacity})'
#
#     def __str__(self):
#         if self.on:
#             status = 'on'
#         else:
#             status = 'off'
#         return f'The fountain contains {self.amount} liters of water and is {status}'
#
#
#
#     def add(self, liters: int):
#         self.amount += liters
#         if self.amount > self.capacity:
#             self.amount = self.capacity
#         elif self.amount <= 0:
#             self.amount = 0
#             self.on = False
#
#     def toggle(self):
#         if self.on:
#             self.on = False
#         elif self.amount > 0:
#             self.on = True
#         else:
#             print('You cannot start an empty fountain.')
#
#     def look(self):
#         print(f'The fountain contains {self.amount} liters of water.')
#         if self.on:
#             print('The fountain is on.')
#         else:
#             print('The fountain is off.')


#
# class Player:
#
#     def __init__(self, name: str):
#
#         self.name = name
#         self.wins = 0
#         self.losses = 0
#
#     def __repr__(self):
#         return f'Player({self.name})'
#
#     def __str__(self):
#         return f'Player {self.name} has {self.wins} wins and {self.losses} losses.'
#
#     def beats(self, other: 'Player'):
#         self.wins += 1
#         other.losses += 1
