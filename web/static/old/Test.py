from Passenger import *
from Elevator import *
from Building import *
import time

def main():
    # e = Elevator(5)
    #
    # e.add_passenger(Passenger(101, 1, 3, 90))
    # e.add_passenger(Passenger(297, 1, 2, 150))
    # e.add_passenger(Passenger(311, 1, 5, 3))
    #
    # for i in range(20):
    #     time.sleep(2)
    #     e.move()
    #     print(e.get_current_floor())

    b = Building(10, 30)
    b.run()

main()