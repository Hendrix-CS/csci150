# Is this big enough can you read me? =D
# This is a comment, Python will ignore me

# Step 0: tell the user the purpose of the program
print("Hello and welcome to the box-o-matic!  Please tell me")
print("the dimensions of your box and I will do the rest!")
print()

# Step 1: ask the user for width
width_str: str = input("Please enter the width of your box in inches: ")

# ask for height
height_str: str = input("Please enter the height of your box in inches: ")

# ask for depth
depth_str: str = input("Please enter the depth of your box in inches: ")

width:  float = float(width_str)
height: float = float(height_str)
depth:  float = float(depth_str)

volume: float = width * height * depth

print()
print("The volume of your box is " + str(volume) + " cubic inches.")
