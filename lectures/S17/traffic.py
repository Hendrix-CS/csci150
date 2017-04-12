# Traffic light
#
# - Keep track of a current color.
# - Can switch to the next color.


# Implementation #1: string variable holding color
# Pros: very simple
# Cons: tedious, difficult to change.
class TrafficLight:
    # Has a variable 'color' which is a string.

    # Create a red traffic light.
    def __init__(self):
        self.color = 'red'

    # Output the current color of the traffic light as a string.
    def current_color(self):
        return self.color

    # Change to the next color.
    def change(self):
        if self.color == 'red':
            self.color = 'green arrow'
        elif self.color == 'green arrow':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'yellow'
        elif self.color == 'yellow':
            self.color = 'red'
        else:
            print("The sky is falling!!")


# Implementation #2
# Pros: dictionaries!!
# Cons: even more tedious.
class TrafficLightDict:

    # color_state  is a dict mapping color names -> True/False

    def __init__(self):
        self.color_state = \
          { 'red' : True, 'yellow' : False, 'green' : False }

    def current_color(self):
        for color in self.color_state:
            if self.color_state[color]:
                return color
        print("The power is probably out!")
        return "blinkingly red"

    def change(self):
        if self.color_state['red']:
            self.color_state['red'] = False
            self.color_state['green'] = True
        elif self.color_state['green']:
            self.color_state['green'] = False
            self.color_state['yellow'] = True
        elif self.color_state['yellow']:
            self.color_state['yellow'] = False
            self.color_state['red'] = True
        else:
            print("The sky is falling!!")
        

# Implementation #3
# Pros: less tedious!  No repetition.
# Cons: still needs if-elif-elif.
#   Even harder to add new colors.
class TrafficLightInt:
    
    # Contains a variable 'color' which is an int 0, 1, or 2.

    def __init__(self):
        self.color = 0

    def current_color(self):
        if self.color == 0:
            return 'red'
        elif self.color == 1:
            return 'green'
        elif self.color == 2:
            return 'yellow'

    def change(self):
        self.color = (self.color + 1) % 3

# Implementation #4
class TrafficLightIntList:
    
    # Contains a variable 'color' which is an int 0, 1, or 2.
    # Contains a list of colors in order.

    def __init__(self):
        self.color = 0
        self.color_list = ['red', 'green arrow', 'green', 'yellow', 'orange', 'purple']

    def current_color(self):
        return self.color_list[self.color]

    def change(self):
        self.color = (self.color + 1) % len(self.color_list)

def main():
    t = TrafficLightIntList()
    for i in range(10):
        print(t.current_color())
        t.change()



    
