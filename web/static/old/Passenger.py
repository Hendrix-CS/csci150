class Passenger:

    # Variables:
    # current_floor: int
    # destination_floor: int
    # in_elevator: bool
    # weight: int
    # ID: int

    def __init__(self, ID: int, current_floor: int, destination_floor: int, weight: int):
        self.ID = ID
        self.current_floor = current_floor
        self.destination_floor = destination_floor
        self.weight = weight

        self.in_elevator = False

    def __repr__(self):
        return ('Passenger(%d, %d, %d, %d)'
                % (self.ID, self.current_floor, self.destination_floor, self.weight))

    def get_ID(self) -> int:
        return self.ID

    def get_current_floor(self) -> int:
        return self.current_floor

    def get_dest_floor(self) -> int:
        return self.destination_floor

    def get_in(self):
        self.in_elevator = True

    def get_out(self):
        self.in_elevator = False