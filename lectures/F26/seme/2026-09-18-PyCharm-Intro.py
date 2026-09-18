# This is our first .py file
#
# First, make sure Python 3 & PyCharm are installed on your computer
#
#
# To check:
# In PyCharm, under the 'File' menu, make a New Project:
# * choose (or create) a folder for CSCI 150
# * Call the project 'Class Code'
# Make sure that Python Version is Python3.something
#
# Click once on the 'Class Code' folder in the Project Window
# File -> New -> Python File -- call it hello_world
#
# A new window will open. Type exactly
print('Hello World')

# Right click (2-finger tap on Mac) and select the Green Triangle --
#
# It should open a new window and print Hello World
# and then say Exit Code 0

# If so, you have downloaded and installed correctly.

# Next: Turn of AI Autocomplete:
# File -> Settings -> Editor -> General -> Inline Completion (or sometimes Code Completion).


# This is a .py file being run through the IDE -- "Integrated Development Environment" PyCharm
#
# PyCharm works differently from Kaggle
# * Kaggle is cell-based -- individual cells are run one at a time
# * you have a 'Markdown' ability -- can write text easily
#
# A .py file in PyCharm runs the *entire* file, top to bottom

# -- Note -- the '#' is the comment character -- it makes the
#     interpreter ignore these lines

# The following lines are commented out
#  You can highlight them and then uncomment by
#  Ctrl /    (that is Control Forward Slash)
#  On  Mac, I think it is the Command Key and forward slash

# def g(z: int):
#     z =  z * 3
#     print(z)
#
#
# def f(x: int):
#     g(x)
#     g(x + 2)
#     print(x)
#
#
# f(3)
#
#
# def alice(z : int) -> int:
#     if z > 0:
#         return z * 2
#     else:
#         return z + 10
#
# def bob(x : int, y : int) -> int:
#     if y < x:
#         return alice(x) + alice(y)
#     else:
#         return alice(x + y)
#
# def main2():
#     print(bob(6,7))
#
# main2()