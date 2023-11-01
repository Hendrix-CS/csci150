class Car:

    # What does a Car object "know", i.e. what data should we store/keep track of about a car?
    # - horsepower
    # - color
    # - oil level
    # - miles driven
    # - speed in mph
    # - rpm

    def __init__(self, horsepower: int, color: str, oil_level: float):
        self.horsepower = horsepower
        self.color = color
        self.oil_level = oil_level
        self.miles_driven = 0
        self.speed = 0
        self.rpm = 0

    # What things can a car "do", i.e. what methods should we create?
    def drive(self, miles: int):
        self.miles_driven += miles
        self.oil_level -= 0.01 * miles

    def needs_oil_change(self) -> bool:
        return self.oil_level < 1