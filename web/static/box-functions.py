###############################
# Compute the volume of a box
#
# Copyright 2018 CSCI 150
###############################

# Inputs:
#   - prompt: string to show to the user
# Repeatedly prompts the user for an int
# until they enter a valid one, then returns it.
def int_input(prompt: str) -> int:
    valid = False
    while not valid:
        s = input(prompt)
        if s.isdigit():
            valid = True
        else:
            print("That is not an int, try again!")
    return int(s)

# Inputs: ...
# Computes the volume of a box.
def compute_volume(l: int, w: int, h: int) -> int:
    # volume = l * w * h
    # return volume

    return l * w * h

def print_volume(l: int, w: int, h: int):
    volume = compute_volume(l, w, h)

    print("The volume of your box (in cubic units) is " + str(volume) + ".")

def main():
    print("Welcome to the Box Calculator!!!11!")

    width  = int_input("What is the width of your box? ")
    length = int_input("What is the length of your box? ")
    height = int_input("What is the height of your box? ")

    print_volume(length, width, height)

    diagonal = (length**2 + width**2 + height**2)**(1/2)

    print("The body diagonal of your box is " + str(diagonal) + " units.")

main()
