# Reminders
#
# * Homework #2 Due Today -- Booleans & Conditionals
# * Quiz #2 on Friday
# * PROJECT #1 Assigned Today -- due Wednesday, Feb 25
#   (see link on course website for details)

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


# Finally:
# Go to the course website and *download* the .py file for today (that's actually *this* file).
# Put that file into your Course Code folder
# Open this file and run. It should print:

#Hello World
#Hello there.
#Hello there.
#Hello there.
#4
#
#Process finished with exit code 0


def aa():
    print('Hello there.')


def bb(x: int) -> int:
    if x > 5:
        aa()
        return x - 9

    else:
        if x == -1:
            aa()
            aa()
            return x - 1
        else:
            return x + 5
            aa()


# main() *NEVER* takes any parameters, and never returns anything
# also, no function *EVER* calls main()

def main():
    x = bb(8)
    y = bb(x)
    z = bb(2)
    print(x + y + z)


main()
