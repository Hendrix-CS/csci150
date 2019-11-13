from typing import *
from Person import *

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

    def __init__(self):
        self.passengers: List[Person] = []
        self.current_floor = 1
        self.pushed_buttons = []
        self.ascending = True

    # change_floor
    def change_floor(self):
        if self.ascending:
            self.current_floor += 1
            print("Going up!")
        else:
            self.current_floor -= 1
            print("Going down!")

        self.remove_push()
        self.release_passengers()

    # push_button: add a button to the list of
    # pushed buttons, if it is not already pushed
    def push_button(self, button: int):
        if button not in self.pushed_buttons:
            self.pushed_buttons.append(button)

    # board_passenger
    def board_passenger(self, p):
        self.passengers.append(p)
        # Maybe have p push the button for their
        # desired floor, if not already pushed

    # release_passengers: let out anyone who wants to get
    #   out.
    def release_passengers(self):

        # Keep the people who want to stay on
        new_passenger_list: List[Person] = []
        for p in self.passengers:
            if p.get_desired_floor() != self.current_floor:
                new_passenger_list.append(p)
            else:
                p.get_off_elevator()

        self.passengers = new_passenger_list

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
