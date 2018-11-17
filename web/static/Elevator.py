from typing import *
from Passenger import *

class Elevator:

    # going_up (up/down): bool
    # destinations: List[int]
    # total_weight: int
    # weight_limit: int
    # current_floor: int
    # door_open: bool
    # max_floor: int
    # passengers: List[Passenger]

    def __init__(self, max_floor: int):
        self.max_floor = max_floor

        self.going_up = True
        self.current_floor = 1
        self.passengers = []

    # Move one floor in the current direction
    # Let any passengers out who want to get out
    # Turn around if @ top or bottom floor.
    def move(self):
        if self.going_up:
            self.current_floor += 1
        else:
            self.current_floor -= 1

        print("FLOOR %d" % self.current_floor)

        if self.current_floor == 1:
            self.going_up = True
        elif self.current_floor == self.max_floor:
            self.going_up = False

        new_passengers: List[Passenger] = []
        for p in self.passengers:
            if p.get_dest_floor() == self.current_floor:
                print("Passenger %d gets off" % p.get_ID())
                p.get_out()
            else:
                new_passengers.append(p)
        self.passengers = new_passengers

    # Let a passenger on the elevator
    def add_passenger(self, p: Passenger):
        self.passengers.append(p)
        p.get_in()

    # Return the current floor
    def get_current_floor(self):
        return self.current_floor