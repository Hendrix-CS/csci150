# Defining our own functions!

def say_hi_a_lot():
    say_hi_twice()
    print("hi hi")
    say_hi_twice()

def say_hi_twice():
    say_hi()
    say_hi()

# Keyword 'def' for defining a function
def say_hi():
    print("Hello, CSCI 150!")
    print("This is a function")
    print(3/0)

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

# Convert a temperature in Fahrenheit into a qualitative adjective.
def F_to_qualitative(temp_F: float) -> str:
    if temp_F < 32:
        return "freezing"
    elif temp_F < 65:
        return "mild"
    elif temp_F < 85:
        return "worm"
    elif temp_F < 100:
        return "uncomfortable"
    else:
        return "dead"


# Prompts the user for the temperature in Celsius, converts it to F, then makes
# an appropriate comment about the weather.
def discuss_weather():
    my_temp_C = float(input("What is the temp in degrees C? "))
    F = C_to_F(my_temp_C)
    weather_str = F_to_qualitative(F)
    print("My, it's very " + weather_str + " today, don't you think?")

def discuss_weather2():
    my_temp_C = float(input("What is the temp in degrees C? "))
    weather_str = F_to_qualitative(C_to_F(my_temp_C))
    print("My, it's very " + weather_str + " today, don't you think?")

def discuss_weather3():
    my_temp_C = float(input("What is the temp in degrees C? "))
    print("My, it's very " + F_to_qualitative(C_to_F(my_temp_C)) + " today, don't you think?")

def discuss_weather4():
    print("My, it's very " + F_to_qualitative(C_to_F(float(input("What is the temp in degrees C? ")))) + " today, don't you think?")