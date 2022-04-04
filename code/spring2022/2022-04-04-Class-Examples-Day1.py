from typing import *

# Reminders:
# Project #2 is due *next* Monday
# Homework #8 (Heap Tracing) is due this Wednesday
# Later today (or tomorrow) after I have gone through the turned in
#    exam #2 redos, I will send out a grade update to all students by email
#   Please check it and let me know if you have questions

# We start with the Heap Tracing from last time



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

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.amount = 0
        self.on = False

    # def __repr__(self):
    #     return f'Fountain({self.capacity})'

    # def __str__(self):
    #     if self.on:
    #         status = 'on'
    #     else:
    #         status = 'off'
    #     return f'The fountain contains {self.amount} liters of water and is {status}'



    def add(self, liters: int):
        self.amount += liters
        if self.amount > self.capacity:
            self.amount = self.capacity
        elif self.amount <= 0:
            self.amount = 0
            self.on = False

    def toggle(self):
        if self.on:
            self.on = False
        elif self.amount > 0:
            self.on = True
        else:
            print('You cannot start an empty fountain.')

    def look(self):
        print(f'The fountain contains {self.amount} liters of water.')
        if self.on:
            print('The fountain is on.')
        else:
            print('The fountain is off.')



############
# Player class --
# Imagine that we have a group of people who all play head-to-head games
# We wish to keep track of each player's wins and losses
#
#
class Player:

    def __init__(self, name: str):

        self.name = name
        self.wins = 0
        self.losses = 0

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player {self.name} has {self.wins} wins and {self.losses} losses.'

    def beats(self, other: 'Player'):
        self.wins += 1
        other.losses += 1


## We culd expand this to have each player with a win_list and loss_list,
# which would add the other player to the appropriate list


#######################################################################
######################################################################
# Heap Tracing

#
def f1(s: str) -> int:
    if len(s) % 2 == 0:
        return 0
    else:
        return len(s)

def f2(d: Dict[str, int]):
    for key in d:
        d[key] = f1(key)

def main1():
    a = {'alice': 5, 'bob': 9, 'star' : -6, '': 7}
    b = a

    c = {}
    for key in b:
        c[key] = b[key]

    f2(b)

    print(a)
    print(b)
    print(c)

main1()