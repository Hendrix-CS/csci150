# Modelling a traffic light in Python

# 1. What should a traffic light know/remember?
#   - time interval between changes (or multiple intervals)
#   - speed limit
#   X current color
#   - if there is a car waiting
#   - order of colors
#   - color of other lights around it
#   - color of left turn light

# 2. What should a traffic light be able to do?
#   X change colors
#   - sense whether a car is there
#   - flash yellow when a train goes by
#   X report its current color
#   - light up / turn on
#   - report if a light goes out

class TrafficLight:

    # Variables:
    #   - current_color (string)

    def __init__(self):
        self.current_color = "RED"

    # Change to next color in the cycle
    def change(self):
        if self.current_color == "GREEN":
            self.current_color = "YELLOW"
        elif self.current_color == "YELLOW":
            self.current_color = "ORANGE"
        elif self.current_color == "ORANGE":
            self.current_color = "RED"
        elif self.current_color == "RED":
            self.current_color = "GREEN"
        else:
            print "The sky is falling!"  # this should never happen.

    # Report the current color
    # Why bother having this method when we can just
    #   directly reach in and look at current_color?
    def color(self):
        return self.current_color

class TrafficLight2:

    # Variables:
    #   - current_color (string)
    #   - color_dict (dictionary from strings to strings)

    def __init__(self):
        self.current_color = "RED"
        self.color_dict = { "GREEN" : "YELLOW"
                                    , "YELLOW" : "ORANGE"
                                    , "ORANGE" : "RED"
                                    , "RED" : "GREEN" }

    def change(self):
        self.current_color = self.color_dict[self.current_color]

    def color(self):
        return self.current_color

class TrafficLight3:

    # Variables:
    #   - color_list  (list of strings)
    #   - color_index (int  -- index of current color in color_list)

    def __init__(self):
        self.color_list = ["RED", "PURPLE", "GREEN", "YELLOW", "ORANGE"]
        self.color_index = 0  # start with RED

    def change(self):
        self.color_index += 1
        self.color_index %= len(self.color_list)

    def color(self):
        return self.color_list[self.color_index]
        

def main():
    t = TrafficLight3()
    for i in range(10):
        print t.color()
        t.change()


    

