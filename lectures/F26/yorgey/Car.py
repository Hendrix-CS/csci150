from dataclasses import dataclass

@dataclass
class Car:

    gas: float       # Amount of gas in the tank, in gallons
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

    def drive(self, driving_speed: float):
        self.speed = driving_speed
        self.gas -= 1

def main():
    car1 = Car(12, 0, 0)
    car2 = Car(5, 0, 0)
    car1.change_passengers(3)
    car1.drive(30)
    car1.change_passengers(2)
    car2.change_passengers(1)
    car1.fill_gas(1)
    car1.drive(0)
    car1.fill_gas(3)

    print(car1.gas)
    print(car2.passengers)

main()