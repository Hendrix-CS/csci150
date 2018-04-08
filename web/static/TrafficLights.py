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

def main():
    t = TrafficLight()
    print(t.color())
    for i in range(10):
        t.change()
        print(t.color())

main()