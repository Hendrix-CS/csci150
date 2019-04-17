class TrafficLight:

    # Variables:
    #   - current_color: str

    # Variant 1: all traffic lights start as red,
    # so no parameters need to be provided for __init__
    #
    # e.g.  light = TrafficLight()
    def __init__(self):
        self.current_color = 'red'

    # Variant 2: a starting color must be provided
    #
    # e.g.  light = TrafficLight('purple')
    # def __init__(self, init_color: str):
    #     self.current_color = init_color

    # Change to the next color in the cycle
    def change_color(self):
        if self.current_color == 'red':
            self.current_color = 'green'
        elif self.current_color == 'green':
            self.current_color = 'yellow'
        else:
            self.current_color = 'red'

    # Return the current color.
    def get_current_color(self) -> str:
        return self.current_color


class TrafficLight2:

    # Variables:
    #   - color_list: List[str]
    #   - current_color_index: int

    def __init__(self):
        self.color_list = ['red', 'green', 'yellow']
        self.current_color_index = 0

    def get_current_color(self) -> str:
        return self.color_list[self.current_color_index]

    # Change to the next color in the list
    def change_color(self):
        self.current_color_index += 1
        self.current_color_index %= len(self.color_list)

        # if self.current_color_index == len(self.color_list):
        #     self.current_color_index = 0

def main():
    light = TrafficLight2()
    for _ in range(10):
        light.change_color()
        print(light.get_current_color())

main()