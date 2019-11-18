from Elevator import *
from Person import *
from Hotel import *

def main():
    h = Hotel(10, 5, 50)
    for _ in range(50):
        h.step()

main()