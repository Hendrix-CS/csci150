# Traffic lights

# What kind of things should a traffic light know / keep track of (variables)?

  # Current color
  # How much time until switching colors
  # How long the current color has been on
  # Direction
  # Whether it is showing an arrow
  # Whether it is blinking
  # Whether cars are at the light
  # How many lanes there are

# What kind of things should a traffic light be able to do (functions)?

  # Switch colors (either to the next color, or to a specified color)
  # Start/stop blinking
  # Turn on arrow

import time

class TrafficLight:
    # Variables/Fields

    # Every TrafficLight object will store:
    #   - current_color: str

    # Functions/Methods

    def __init__(self):
        self.current_color = "RED"

    # Alternatively, if we provide the color when creating a TrafficLight:
    # def __init__(self, init_color: str):
    #     self.current_color = init_color

    # Switch to the next color
    def cycle(self):
        if self.current_color == 'RED':
            self.current_color = 'GREEN'
        elif self.current_color == 'GREEN':
            self.current_color = 'YELLOW'
        elif self.current_color == 'YELLOW':
            self.current_color = 'ORANGE'
        elif self.current_color == 'ORANGE':
            self.current_color = 'RED'
        else:
            # This should never happen
            print("OH NO!!! Traffic light is " + self.current_color)

    # Report the current color
    def get_current_color(self) -> str:
        return self.current_color


# Version 2: store an index into a list of colors
class TrafficLight2:

    def __init__(self):
        self.current_color_index = 0
        self.color_list = ['RED', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE']

    def cycle(self):
        self.current_color_index += 1
        self.current_color_index = self.current_color_index % (len(self.color_list))

    def get_current_color(self) -> str:
        return self.color_list[self.current_color_index]


# Version 3: store a dictionary that tells us what color comes next
class TrafficLight3:

    def __init__(self):
        self.color_dict = { 'RED': 'GREEN', 'GREEN': 'YELLOW', 'YELLOW': 'ORANGE', 'ORANGE': 'RED', 'PURPLE': 'RED' }
        self.current_color = 'PURPLE'

    def get_current_color(self):
        return self.current_color

    def cycle(self):
        self.current_color = self.color_dict[self.current_color]


def main():
    t = TrafficLight3()
    for i in range(10):
        print(t.get_current_color())
        time.sleep(1)
        t.cycle()

main()