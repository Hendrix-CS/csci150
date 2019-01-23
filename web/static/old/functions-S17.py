# Making our own functions

# def = keyword to define a function
# say_hi is the name of the function
# () means it needs no inputs.

# This is a recipe for how to do something.
def say_hi():
    print("Hello there, CSCI 150!")
    print("This is a function.")

say_hi()    # You ALWAYS NEED PARENTHESES.

def say_hi_twice():
    say_hi()
    say_hi()

# temp_C is the name of the input to C_to_F.
# It is called a "parameter".

# temp_C is a float --- the temperature in Celsius
def C_to_F_bad(temp_C):
    # temp_F is a local variable -- only exists inside the function.
    temp_F = temp_C * 9/5 + 32
    print("The temperature in degrees Fahrenheit in " + str(temp_F))

C_to_F_bad(37)   # 37 is an "argument".

# C_to_F is not as useful as it could be because it can only
# print a specific message, and you can't recover the converted
# value later.

def C_to_F(temp_C):
    temp_F = temp_C * 9/5 + 32
    return temp_F

