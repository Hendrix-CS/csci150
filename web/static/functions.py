# Defining our own functions!

def say_hi_twice():
    say_hi()
    say_hi()

# Keyword 'def' for defining a function
def say_hi():
    print("Hello, CSCI 150!")
    print("This is a function")

# Function with an input
# temp_C is a *parameter*
def C_to_F_msg(temp_C: int):
    F = temp_C * 9 / 5 + 32
    print("The temperature in degrees F is " + str(F) + "!!!")

# To use C_to_F_msg: e.g.   C_to_F_msg(15)
# 15 is an *argument*

# F (or any variable defined inside a function) is *local* --- only
# accessible ("in scope") inside the body of the function.
# Parameters are also local.

# C_to_F_msg should actually be decomposed!  It is doing too much at once.

def C_to_F(temp_C: float) -> float:
    F = temp_C * 9 / 5 + 32
    return F
