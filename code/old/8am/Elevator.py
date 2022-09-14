from typing import *
from Person import *
import random

class Elevator:
    # Variables (fields):
    #   - weight_capacity: int
    #   - X current_weight: int
    #   - XXXXX passengers: List[Person]
    #   - XXXX current_floor: int
    #   - XXXXXX pushed_buttons: List[int]
    #   - X call_buttons: List[int]
    #   - elevator_number: int
    #   - XXXX ascending: bool
    #   - X doors_open: bool
    #   - XX moving: bool

    #   - max_floor: int

    def __init__(self, elevator_num: int, max_floor: int):
        self.number = elevator_num
        self.passengers: List[Person] = []
        self.current_floor = random.randint(1, max_floor)
        self.pushed_buttons = []
        self.ascending = True
        self.max_floor = max_floor

    # change_floor
    def change_floor(self):
        if self.current_floor == 1:
            self.ascending = True
        elif self.current_floor == self.max_floor:
            self.ascending = False

        if self.ascending:
            self.current_floor += 1
            print(f"Elevator {self.number} going up!")
        else:
            self.current_floor -= 1
            print(f"Elevator {self.number} going down!")

        self.remove_push()

    # push_button: add a button to the list of
    # pushed buttons, if it is not already pushed
    def push_button(self, button: int):
        if button not in self.pushed_buttons:
            self.pushed_buttons.append(button)

    # board_passenger
    def board_passenger(self, p: Person):
        self.passengers.append(p)
        self.push_button(p.get_desired_floor())
        p.get_on_elevator(self.number)

    # release_passengers: let out anyone who wants to get
    #   out.  Return True if anyone got out, False otherwise.
    def release_passengers(self) -> bool:
        any_got_off: bool = False
        # Keep the people who want to stay on
        new_passenger_list: List[Person] = []
        for p in self.passengers:
            if p.get_desired_floor() != self.current_floor:
                new_passenger_list.append(p)
            else:
                p.get_off_elevator(self.number)
                any_got_off = True

        self.passengers = new_passenger_list

        return any_got_off

    # change_direction: make the elevator go in
    # the opposite direction.
    def change_direction(self):
        self.ascending = not self.ascending

    # remove_push
    def remove_push(self):
        if self.current_floor in self.pushed_buttons:
            self.pushed_buttons.remove(self.current_floor)

    # remove_all_push
    def remove_all_push(self):
        self.pushed_buttons = []

    def get_current_floor(self):
        return self.current_floor
