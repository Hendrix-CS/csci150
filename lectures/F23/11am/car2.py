
class Car:

    # What things should a Car object "know", i.e. what variables should we keep track of?
    # - gas mileage
    # - speed
    # - tire pressure
    # - oil level
    # - check engine light

    def __init__(self, tire_pressure: float, oil_level: float):
        self.check_engine = False
        self.speed = 0
        self.tire_pressure = tire_pressure
        self.oil_level = oil_level

    # What things should a Car object be able to "do", i.e. what methods should we define?

    def set_speed(self, new_speed: float):
        if new_speed > 100:
            print("That's too fast!")
        else:
            self.speed = new_speed

    def drive_for(self, seconds: int):
        self.oil_level -= seconds * self.speed * 0.01

        if self.oil_level < 1:
            self.check_engine = True
