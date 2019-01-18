# From now on everything should be in a function!

# From now on: every function should have some comments
# before it, with:
#
# - Inputs (& their types), if any
# - Output (& its type), if any
# - Description of what the function does.

# Print a greeting for the user.
def print_greeting():
    print("Welcome to the box-o-matic! Enter your box dimensions")
    print("and I will do the rest!")

# Input: ? none
# Output: int entered by the user
# Repeatedly prompt the user until they enter a valid int.
def int_input(prompt_str):
    valid = False
    while not valid:
        input_str = input(prompt_str)
        valid = input_str.isdigit() or (input_str[0] == '-' and input_str[1:].isdigit())
        if not valid:
            print("That is not an integer.  Try again.")
        
    return int(input_str)

# Inputs: h, w, d are all ints which represent the height, width, and depth
#   in furlongs.
# Output: volume of the box.
def box_volume(h, w, d):
    return h * w * d

# Input: height, width, and depth (ints)
# Computes the volume and displays it to the user.
def tell_volume(height, width, depth):
    volume = box_volume(height, width, depth)

    print("The volume of your box is " + str(volume) + " cubic furlongs.")

def main():
    print_greeting()

    height = int_input("Please enter the height of the box in furlongs: ")
    width = int_input("Please enter the width of the box in furlongs: ")
    depth = int_input("Please enter the depth of the box in furlongs: ")

    tell_volume(height, width, depth)

    surface = 2*width*height + 2*height*depth + 2*width*depth

    print("The surface area is " + str(surface) + " square furlongs.")

    diagonal =  (width**2 + height**2 + depth**2)**(1/2)

    print("The body diagonal is " + str(diagonal) + " furlongs.")

main()
