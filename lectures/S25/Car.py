from dataclasses import dataclass

@dataclass
class Car:

    gas: float       # Amount of gas in the tank, in gallons
    mileage: float   # Mileage on the odometer
    speed: float     # Current speed in miles per hour
    passengers: int  # Number of passengers

    def change_passengers(self, num_passengers: int):
        if self.speed == 0:
            self.passengers = num_passengers
        else:
            print('Stop first, do you want to get killed!?')

    def fill_gas(self, added_gas: float):
        if self.speed == 0:
            self.gas += added_gas
        else:
            print(f"You can't fill up while driving {self.speed} miles per hour!")

    def drive(self, driving_speed: float, driving_time: float):
        self.speed = driving_speed
        miles_driven = driving_speed * driving_time
        self.mileage += miles_driven
        self.gas -= miles_driven / 20
