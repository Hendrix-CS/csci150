
# Functions!

# Define a function called say_hi
def say_hi():
    print("Hello, CSCI 150!")
    print("This is a function.")

# Do ("call") the function, by writing
# the name with parentheses (required!) after it
# say_hi()
# say_hi()

def say_hi_twice():
    say_hi()
    say_hi()

# say_hi_twice()


# C_to_F takes a Celsius temperature as input
# and prints out a message with the temp converted to F.
#
# temp_C is called a "parameter".  Specifying its type
# is optional but not for you.
def C_to_F(temp_C: float):

    # temp_F is *local*, that is, it only exists inside the function,
    # and it goes away when the function is done.
    # Any parameters such as temp_C are also local variables.
    temp_F: float = temp_C * 9 / 5 + 32
    print("The temperature in degrees Fahrenheit is " + str(temp_F) + ".")

# C_to_F_improved takes a Celsius temperature as input
# and returns a float value representing the temperature
# in Fahrenheit.
def C_to_F_improved(temp_C: float) -> float:
    temp_F: float = temp_C * 9/5 + 32
    return temp_F

    # This never happens
    print("At the end of the function!")


# C_to_F_improved(30)