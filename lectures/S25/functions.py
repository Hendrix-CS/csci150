# Functions!

# From now on, all code must be in functions!

# Define some functions

# Inputs in parentheses are called "parameters"
# c2f has one parameter, which is a float called 'degrees_c'.
def c2f(degrees_c: float) -> float:
    # Variables created inside a function are *local*,
    # i.e. they only exist within the function, and cannot
    # be accessed from anywhere outside the function.
    degrees_f = degrees_c * 9/5 + 32
    return degrees_f

def number() -> int:
    return 3

def main():
    print("Hello!")
    do_stuff()
    # print(number)  # to call a function, it must have parentheses after the name!
    print(number())
    # When we call a function, the inputs we actually give it are called "arguments"
    # In this case, 37 is an argument to c2f.

    # This degrees_f and the one in c2f are completely separate variables
    # that happen to have the same name.
    degrees_f = 5
    degrees_f = c2f(37)
    print(degrees_f)

def funA(n: int):
    print(n * 3 + 17)
    print("In funA")

def funB(q: int):
    print(q + 3 / 0)
    print("Divided by zero")

def do_stuff():
    print("Doing stuff")
    funA(12)
    funB(3)

main()

