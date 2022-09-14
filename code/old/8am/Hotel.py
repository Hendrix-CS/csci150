from Person import *
from Elevator import *
import random

class Hotel:

    # Variables:
    #   - continental breakfast
    #   - max_floor: int
    #   - num_elevators: int
    #   - waiting_people: Dict[int, List[Person]]
    #   - elevators: List[Elevator]

    # Other hotel-ish things we could model:
    #   - occupancy: int
    #   - rooms

    def __init__(self, max_floor: int, num_elevators: int, num_people: int):
        self.max_floor = max_floor
        self.num_elevators = num_elevators

        self.elevators = []
        for i in range(self.num_elevators):
            self.elevators.append(Elevator(i, self.max_floor))

        self.waiting_people = {}
        for floor in range(1, self.max_floor+1):
            self.waiting_people[floor] = []

        for _ in range(num_people):
            p = Person(random.randint(1, self.max_floor), random.randint(1, self.max_floor), random.randint(10, 1000))
            self.waiting_people[p.get_origin_floor()].append(p)

    # For each elevator, let people get on if anyone is waiting, or move it one floor.
    def step(self):

        print("--------------------------------------")
        # For each elevator:
        for e in self.elevators:

            waiting = self.waiting_people[e.get_current_floor()]

            # Check if anyone is waiting to get off
            if e.release_passengers():
                pass

            # Check if anyone is waiting on this elevator's floor
            elif waiting:   # if len(waiting) > 0:
                # Put all the people on the elevator
                for p in waiting:
                    e.board_passenger(p)
                # Remove them from the list of waiting people
                self.waiting_people[e.get_current_floor()] = []

            else:
                e.change_floor()
