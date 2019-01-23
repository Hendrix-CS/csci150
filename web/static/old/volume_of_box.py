###################
# Volume of a Box
# Example from Class
# August 29, 2018
#
# Takes in user input of width, height,depth
# and returns the volume of that box

## Input the dimensions and convert to float
width_str:str = input('Enter the Width of the Box: ')
width = float(width_str)

height_str:str = input('Enter the Height of the Box: ')
height = float(height_str)

depth_str:str = input('Enter the Depth of the Box: ')
depth = float(depth_str)

print('The box volume is ' + str(width * height * depth) + '.')