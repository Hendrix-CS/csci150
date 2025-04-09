# A fountain has:
#   - a capacity (= total amount of water it can hold)
#   - a current amount of water
#   - whether it is currently running
#
# Things a fountain can do:
#
#   - Turn on/off
#   - Fill or drain water
#   - Print out its current status

from dataclasses import dataclass

@dataclass
class Fountain:

    # 1. list all the fields we want (= variables stored in a Fountain object)
    capacity: int           # capacity in liters
    water: int              # current amount of water in liters
    running: bool = False   # whether it is running - defaults to False.

    # 2. Write some methods, i.e. things a Fountain object can do.

    # Turn the fountain on
    def turn_on(self):
        # Make sure fountain is not empty before turning on
        if self.water > 0:
            self.running = True
        else:
            print("Can't turn on an empty fountain!")

    def turn_off(self):
        self.running = False

    def print_status(self):
        if self.running:
            print('sploosh!')

        print(f'The fountain contains {self.water}L, and has a capacity of {self.capacity}L.')

    def modify_water(self, delta: int):
        self.water += delta
        if self.water > self.capacity:
            print(f"{self.water - self.capacity} liters slosh over the side!")
            self.water = self.capacity
        elif self.water <= 0:
            self.running = False
            self.water = 0

