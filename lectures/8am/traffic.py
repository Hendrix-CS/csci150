# Traffic light
#
# Go support the volleyball team who are
# hosting the SAA tournament this weekend
# First game today at 1pm
#
# How would you model it in Python?
# What functions should it have?
# How would it work?

# Possible functions:
#   - separate red, green, yellow light functions
#   - interval function
#   - sensor
#   - change to next color
#   - say what the current color is
#   - run
# Variables / state:
#   - current color
#   - timer (time left until next change?)


# Version 1:
#   - easy to write
#   - tedious (imagine cycling through 20 colors)
#   - difficult to change
class TrafficLight:

    # Variables:
    #   - current_color (string)

    # Create a new red traffic light
    def __init__(self):
        self.current_color = "RED"

    # Change to next color
    def change(self):
        if self.current_color == "RED":
            self.current_color = "GREEN"
        elif self.current_color == "GREEN":
            self.current_color = "YELLOW"
        elif self.current_color == "YELLOW":
            self.current_color = "ORANGE"
        elif self.current_color == "ORANGE":
            self.current_color = "RED"
        else:
            print "The sky is falling!!"  # This should never happen

    # Return the current color
    def color(self):
        return self.current_color

# Version 2:
# Use a dictionary of colors
class TrafficLight2:

    # Variables:
    #   - current_color
    #   - color_dict

    def __init__(self):
        self.current_color = "RED"
        self.color_dict = \
          { "RED" : "GREEN",
            "GREEN" : "YELLOW",
            "YELLOW" : "ORANGE",
            "ORANGE" : "RED" }

    def change(self):
        self.current_color = self.color_dict[self.current_color]

    def color(self):
        return self.current_color

# Version 3: list of colors
class TrafficLight3:

    # Variables:
    #   - color_list
    #   - current_index

    def __init__(self):
        self.color_list = ["RED", "GREEN", "YELLOW", "ORANGE"]
        self.current_index = 0

    def change(self):
        self.current_index += 1
        self.current_index %= len(self.color_list)

    def color(self):
        return self.color_list[self.current_index]

def main():
    t = TrafficLight3()
    print t.color()
    for i in range(10):
        t.change()
        print t.color()

main()
