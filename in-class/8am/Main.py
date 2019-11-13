from Elevator import *
from Person import *

def main():
    e = Elevator()

    p1 = Person(1, 5, 100)
    p2 = Person(1, 3, 250)
    p3 = Person(1, 2, 7000)
    p4 = Person(1, 2, 70)

    e.board_passenger(p1)
    e.board_passenger(p2)
    e.board_passenger(p3)
    e.board_passenger(p4)

    for _ in range(10):
        e.change_floor()

main()