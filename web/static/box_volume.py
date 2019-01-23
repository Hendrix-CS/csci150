######################################
#
# Box volume calculator
# CSCI 150, Spring 2019
#
######################################

print('Welcome to the box volume calculator!')

height_str: str = input('What is the height of your box? ')
height: float = float(height_str)

width: float = float(input('What is the width of your box? '))

depth: float = float(input('What is the depth of your box? '))

volume: float = height * width * depth

print('The volume of your box is ' + str(volume) + ' cubic units.')