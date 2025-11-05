# Fountain example

from dataclasses import dataclass

@dataclass
class Fountain:

    # Fields, aka things a Fountain object "knows", aka what information we
    # will store about a fountain.
    capacity: int         # Total amount of water it can hold (L)
    current_water: int    # Amount of water it currently holds (L)
    running: bool = False # Is it currently turned on?  Defaults to False,
                          #   means we can optionally omit this when creating a new
                          #   Fountain object.

    # Methods, aka things a Fountain can do / things we can do with/to a Fountain.
    def adjust_water(self, water: int):
        self.current_water += water
        if self.current_water > self.capacity:
            print(f"Splash! {self.current_water - self.capacity}L of water overflowed!")
            self.current_water = self.capacity
        elif self.current_water < 0:
            self.current_water = 0

    # Switch from not running to running or vice versa
    def switch(self):
        if self.running:
            self.running = False
        else:
            if self.current_water == 0:
                print("You can't turn on an empty fountain!")
            else:
                self.running = True

    # Print out the status of the fountain
    def print_status(self):
        print(f'The fountain contains {self.current_water}L out of a capacity of {self.capacity}L')
        if self.running:
            print('Sploosh!!')

    def is_running(self) -> bool:
        return self.running