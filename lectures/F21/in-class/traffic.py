from dataclasses import dataclass
from typing import *

@dataclass
class TrafficLight:

    # current_color always starts out
    #   as 'RED'.
    current_color: str = 'RED'

    # Tell the traffic light to change
    # to the next color in the cycle.
    def change(self):
        if self.current_color == 'RED':
            self.current_color = 'GREEN'
        elif self.current_color == 'GREEN':
            self.current_color = 'YELLOW'
        elif self.current_color == 'YELLOW':
            self.current_color = 'RED'
        else:
            # This should never happen
            print('Oh noes!!!1')

    # Ask the traffic light what its
    #   current color is.
    def get_current_color(self) -> str:
        return self.current_color

@dataclass
class TrafficLight2:

    colors: List[str]
    current_index: int = 0

    def get_current_color(self):
        return self.colors[self.current_index]

    def change(self):
        self.current_index += 1
        if self.current_index == len(self.colors):
            self.current_index = 0

        # Alternative:
        # self.current_index = \
        #     (self.current_index + 1) % len(self.colors)


def main():
    t: TrafficLight2 = \
        TrafficLight2(['RED','GREEN','YELLOW'])

    for i in range(10):
        print(t.get_current_color())
        t.change()

main()