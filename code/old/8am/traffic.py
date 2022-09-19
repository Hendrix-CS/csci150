import time

# Traffic lights
#   - What things do they "know" (i.e. what data do they
#     store/keep track of)?
#
#     - protected turn? (boolean)
#     - flashing or solid? (boolean)
#     - what color is it? (str)
#     - what time is it? (int / time)
#     - amount of time left before/since changing? (int / time)
#     - which streets have more traffic? (list of ? ints?)
#         (dictionary?)
#   - What things can they "do"?  What questions can you ask
#     them?
#
#     - change color
#     - change between flashing and solid
#     - turn arrow on/off
#     - start timer
#     - check sensor for motion
#     - take picture of car / store information

class TrafficLight:
    # Variables/fields/things it "knows":
    #   - current_color: str

    # Create a new TrafficLight object
    # with a given initial color
    def __init__(self, init_color: str):
        self.current_color = init_color

    # Alternatively: all TrafficLight objects
    # start out red
    # def __init__(self):
    #     self.current_color = 'RED'

    # Report the current color.
    def get_current_color(self) -> str:
        return self.current_color

    # Change to the next color.
    def change(self):
        if self.current_color == 'RED':
            self.current_color = 'GREEN'
        elif self.current_color == 'GREEN':
            self.current_color = 'YELLOW'
        elif self.current_color == 'YELLOW':
            self.current_color = 'RED'

from typing import *

class TrafficLight2:

    def __init__(self, color_list: List[str]):
        self.color_list = color_list
        self.index = 0

    def get_current_color(self):
        return self.color_list[self.index]

    def change(self):
        self.index += 1
        self.index %= len(self.color_list)

def main():
    t = TrafficLight2(['RED','GREEN','YELLOW','ORANGE'])
    for _ in range(15):
        print(t.get_current_color())
        time.sleep(0.5)
        t.change()

main()