from Passenger import *
from Elevator import *

import random
import time

class Building:

    # Variables:
    # num_floors: int
    # num_elevators: int
    # waiting_passengers: Dict[int, List[Passenger]]
       # key = floor
       # value = passengers waiting on that floor
    # elevator: Elevator
       # (later, List[Elevator])

    def __init__(self, num_floors: int, num_passengers: int):
        self.num_floors = num_floors
        self.elevator = Elevator(self.num_floors)

        self.waiting_passengers = {}

        for i in range(num_passengers):
            p: Passenger = Passenger(i, random.randint(1, num_floors), random.randint(1, num_floors), random.randint(1, 300))

            # Create the list for p's floor if it doesn't already exist
            if p.get_current_floor() not in self.waiting_passengers:
                self.waiting_passengers[p.get_current_floor()] = []

            # Add p to the line of passengers waiting on that floor
            self.waiting_passengers[p.get_current_floor()].append(p)

    # Move the elevator and put waiting people on it
    def update(self):

        # Move the elevator one floor (and let passengers off)
        self.elevator.move()

        # Put people on the elevator
        if self.elevator.get_current_floor() in self.waiting_passengers:
            for p in self.waiting_passengers[self.elevator.get_current_floor()]:
                print("Passenger %d gets on the elevator" % p.get_ID())
                self.elevator.add_passenger(p)

        # No one is waiting on that floor anymore
        self.waiting_passengers[self.elevator.get_current_floor()] = []

    def run(self):
        while True:
            self.update()
            time.sleep(1)