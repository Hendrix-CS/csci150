###############################
# Compute the volume of a box
#
# Copyright 2018 CSCI 150
###############################

print("Welcome to the Box Calculator!!!11!")

width  = float(input("What is the width of your box? "))
length = float(input("What is the length of your box? "))
height = float(input("What is the height of your box? "))

volume = length * width * height

print("The volume of your box (in cubic units) is " + str(volume) + ".")

diagonal = (length**2 + width**2 + height**2)**(1/2)

print("The body diagonal of your box is " + str(diagonal) + ".")