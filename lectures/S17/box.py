# This is a comment.  Python will ignore it.
# CSCI 150, Spring 2017
# Copyright (c) 2017, CSCI 150

# Print a greeting
print("Welcome to the box-o-matic! Enter your box dimensions")
print("and I will do the rest!")

# Ask user for the height of the box
# & remember it
height_str = input("Please enter the height of the box in furlongs: ")

# note that height_str is a str:
# print(type(height_str))

height = int(height_str)

# To convert to an int, use int(...)

# Ask user for the width of the box
# & remember it
width_str = input("Please enter the width of the box in furlongs: ")

width = int(width_str)

# Ask user for the depth of the box
# & remember it
depth_str = input("Please enter the depth of the box in furlongs: ")

depth = int(depth_str)

# Compute the volume
volume = height * width * depth

# Display the result to the user
print("The volume of your box is " + str(volume) + " cubic furlongs.")

# Compute the surface area
surface = 2*width*height + 2*height*depth + 2*width*depth

print("The surface area is " + str(surface) + " square furlongs.")

# Compute the body diagonal
diagonal =  (width**2 + height**2 + depth**2)**(1/2)

print("The body diagonal is " + str(diagonal) + " furlongs.")
