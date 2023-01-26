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
# So, a = Fountain(100) would create a Fountain object which is
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
#       if the fountain is off and empty, toggle will not turn it on. Instead,
#       a message to the user should be printed
#
#   look()  - prints (not returns) a string which describes the state of the fountain.

class Fountain:    # by convention, we start names of classes with capital letters
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.water = 0
        self.running = False

    def add(self, liters: int):
        if self.water + liters > self.capacity:
            self.water = self.capacity
        elif self.water + liters <= 0:
            self.water = 0
            self.running = False
        else:
            self.water += liters

    def toggle(self):
        if self.water == 0 and self.running == False:
            pass
        else:
            self.running = not self.running    # Toggle whether it is on

        # Alternatively:
        #
        # if not (self.water == 0 and self.running == False):
        #     self.running = not self.running    # Toggle whether it is on

    def look(self):
        if self.running:
            print("Sploosh! The fountain is on.")
        else:
            print("The fountain is off.")

        print(f'It contains {self.water}/{self.capacity} liters.')

################################################################################

from typing import *

def main():
    fountains: List[Fountain] = []
    for c in [10, 20, 30, 40]:
        fountains.append(Fountain(c))

    for f in fountains:
        f.add(25)
        f.toggle()

    for f in fountains:
        f.look()

main()