# Modelling a traffic light using a class

# Variables / things a traffic light knows/remembers/stores

#   - Which light is currently on
#   - Color of current light
#   - Time until it changes
#   - What kind of shapes it contains?
#   - Time of day
#   - Order of colors
#
# Functions / things a traffic light can do
#
#   - Change color
#   - Validate state
#   - Take a picture
#   - CATCH CRIMINALS
#   - Wait
#   - Detect emergency vehicles (!!)
#   - Blink red (panic!)
#   - Activate crosswalk

# We will
#   - keep track of current color
#   - be able to change to next color

from typing import *

class TrafficLight:

    # Variables:
    #   - current_color: str

    # Create a new red traffic light
    def __init__(self):
        self.current_color = "RED"

    # Return the current color
    def color(self) -> str:
        return self.current_color

    # Change to the next color
    def change(self):
        if self.current_color == 'GREEN':
            self.current_color = 'YELLOW'
        elif self.current_color == 'YELLOW':
            self.current_color = 'RED'
        elif self.current_color == 'RED':
            self.current_color = 'GREEN'
        else:
            print("PANIC!!!")

# Another implementation using a list of colors
class TrafficLight2:
    # Variables:
    #   - current_color_index: int  (index into the list of colors)
    #   - color_list: List[str]

    # What parameters does __init__ need?
    def __init__(self):  # , color_list: List[str]):
        self.current_color_index = 0
        self.color_list = ["RED", "GREEN", "YELLOW"]

    def color(self) -> str:
        return self.color_list[self.current_color_index]

    def change(self):
        self.current_color_index += 1
        self.current_color_index %= len(self.color_list)

    def add_color(self, new_color: str):
        self.color_list.append(new_color)

def main():
    t = TrafficLight2()
    print(t.color())
    for i in range(10):
        t.change()
        print(t.color())

    t.add_color("PURPLE")
    for i in range(10):
        t.change()
        print(t.color())

main()