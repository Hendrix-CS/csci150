# Example: fountain
#
# What information does a fountain keep track of?
#
#   - on or off
#   - amount of water
#
# What can a fountain do?
#
#   - turn it on (only if amount of water > 0)
#   - turn it off
#   - add water (total water can't become negative)
#   - observe (print out a message saying whether it is running + how much water it contains)

from dataclasses import dataclass

@dataclass
class Fountain:

    on: bool
    amount_of_water: float

    def turn_on(self):
        if self.amount_of_water > 0:
            self.on = True
        else:
            print("Can't turn on empty fountain!")
