
class Person:
    # Variables:
    #   - origin_floor: int
    #   - desired_floor: int
    #   - weight: int

    def __init__(self, origin_floor: int, dest_floor: int, weight: int):
        self.origin_floor = origin_floor
        self.desired_floor = dest_floor
        self.weight = weight

    def get_origin_floor(self) -> int:
        return self.origin_floor

    # Get the person's desired destination floor
    def get_desired_floor(self) -> int:
        return self.desired_floor

    # Get the person's weight (in
    def get_weight(self) -> int:
        return self.weight

    # Get on the elevator and print a message.
    def get_on_elevator(self, elevator_num: int):
        print(f"Person with weight {self.weight} getting on elevator #{elevator_num} at floor {self.origin_floor}")

    # Get off the elevator and print a message.
    def get_off_elevator(self, elevator_num: int):
        print(f"Person with weight {self.weight} getting off elevator #{elevator_num} at floor {self.desired_floor}")

    # Return a string describing the person
    def __str__(self):
        return f"Person with weight {self.weight}, {self.origin_floor} -> {self.desired_floor}"