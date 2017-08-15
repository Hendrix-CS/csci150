# Making our own functions

# def = keyword to define a function
# say_hi is the name of the function
# () means it needs no inputs.

def say_hi_twice():
    say_hi()
    say_hi()

# This is a recipe for how to do something.
def say_hi():
    print("Hello there, CSCI 150!")
    print("This is a function.")
    print("Magic: " + str(1/0))

# say_hi()    # You ALWAYS NEED PARENTHESES.


def func3():
    say_hi_twice()
    print ("here")
    say_hi_twice()

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

def C_to_F_short(temp_C):
    return temp_C * 9/5 + 32
    # print("The temperature is " + str(temp_C))  # does nothing

# Input: temperature in degrees F (float)
# Output: a word to describe that temperature (string)
def F_to_qualitative(temp_F):
    if temp_F < -60:
        return 'dead'  
    elif temp_F < 32:
        return 'freezing'
    elif temp_F < 50:
        return 'cold'
    elif temp_F < 75:
        return 'nice! temperate'
    elif temp_F < 90:
        return 'hot'
    elif temp_F < 120:
        return 'scorching'
    else:
        return 'dead'

# Prompts the user for the temperature in degrees C,
# then makes a comment about the weather
def weather_chat():
    C_input = float(input("What is the temperature in degrees C? "))
    temp_F = C_to_F(C_input)
    word = F_to_qualitative(temp_F)
    print("Gee, you must feel " + word + " today.")

def weather_chat2():
    C_input = float(input("What is the temperature in degrees C? "))
    temp_F = C_to_F(C_input)
    print("Gee, you must feel " + F_to_qualitative(temp_F) + " today.")

def weather_chat3():
    C_input = float(input("What is the temperature in degrees C? "))
    print("Gee, you must feel " + F_to_qualitative(C_to_F(C_input)) + " today.")

# DO NOT TRY THIS AT HOME
def weather_chat4():
    print("Gee, you must feel " + F_to_qualitative(C_to_F(float(input("What is the temperature in degrees C? ")))) + " today.")
