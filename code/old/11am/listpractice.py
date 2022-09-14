from typing import *

def explode_list(t: List[str]):
    n = 0
    while n < len(t):
        print(t[n])
        n += 1

def adding():
    animals = ["okapi", "tarsier", "hippo", "parrot", "mouse"]

    # Somehow get three copies of "lemur" at the end
    # ["okapi", "tarsier", "hippo", "parrot", "mouse", "lemur", "lemur", "lemur"]

    # WORKS!!!
    #x = 0
    #while x < 3:
    #    animals.append("lemur")
    #    x += 1

    # WORKS!!!
    #animals = ["okapi", "tarsier", "hippo", "parrot", "mouse", "lemur", "lemur", "lemur"]

    # BOOO
    #animals[0] = "lemur"
    #animals[1] = "lemur"
    #animals[2] = "lemur"

    # BOOO
    #animals.append("lemur" + "lemur" + "lemur")

    # BOOO
    # animals.append("lemur" * 3)

    # IT WORKS!
    #x = 0
    #while x < 3:
    #    animals = animals + ["lemur"]
    #    x += 1

    # WORKS!
    #lemur = ["lemur"] * 3
    #animals += lemur

    x = 0
    while x < 3:
        animals.append(input("type lemur: "))
        x += 1

    print(animals)

adding()

