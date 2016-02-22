# CSCI 150
# Feb 10 2016
# Functions

def say_hi_twice():
    say_hi()
    say_hi()

def say_hi():
    print "Hello there, CSCI 150!"
    print "This is a function."

# Order of function definitions does not matter

say_hi_twice()

# Why functions?

# * Makes code shorter --- no copy & paste repeated things
# * Helps organize complex code
# * Easier to debug
#    - Fixes only have to be made in one place
#    - Easier to identify & test bugs separately
# * Reuse

# NOTE: you do not need to use functions on the project!

# Functions with inputs!

def C_to_F(temp_C):      # header
                                        # temp_C is a "parameter"
                                        # i.e. name of an input to the function
    F = 1.8*temp_C + 32
    print "The temperature in degrees Fahrenheit is", F

# How to call a function with an input:
C_to_F(15)     # 15 is called an "argument"
C_to_F(23 + 98*7 - 100)
C_to_F(-40)

# NOTE: parameters are "local".
# Variables defined inside a function are also "local".
# Local variables/parameters are only defined inside the
#   function.

# Version that does not print anything, just gives back
#   F as an output.  Try to design functions that do
#   only ONE JOB.  C_to_F was doing two jobs: converting
#   AND printing on the screen.
def better_C_to_F(temp_C):
    F = 1.8*temp_C + 32
    # F has the same name as F from C_to_F but they
    #   are completely unrelated.

    return F     # stop and immediately give F as output

# Book calls these "fruitful functions" (Chapter 5)
    
def better_C_to_F_2(temp_C):
    F = (1.8*temp_C + 32) / 0
    # F has the same name as F from C_to_F but they
    #   are completely unrelated.

    return F     # stop and immediately give F as output
    print "Done converting!"   # this never happens!

def better_C_to_F_3(temp_C):
    return 1.8*temp_C + 32
    # this does the same thing as better_C_to_F

def F_to_qualitative(temp_F):
    if temp_F < 32:
        return "freezing"
    elif temp_F < 60:
        return "cold"
    elif temp_F < 80:
        return "warm"
    elif temp_F < 100:
        return "hot"
    else:
        return "ouchies"

# Prompt the user for temp in F
# Make a comment like "it is warm today".
def discuss_weather_in_US():
    temp_F = int(raw_input("What is the temperature in degrees F? "))
    word = F_to_qualitative(temp_F)
    print "Hmm, it is very " + word + " today, don't you think?"


# Prompt the user for temp in C
# Make a comment like "it is warm today".
def discuss_weather_in_metric():
    temp_C = int(raw_input("What is the temperature in degrees C? "))
    temp_F = better_C_to_F_2(temp_C)
    word = F_to_qualitative(temp_F)
    print "Hmm, it is very " + word + " today, don't you think?"

# Prompt the user for temp in C
# Make a comment like "it is warm today".
def discuss_weather_in_metric_2():
    temp_C = int(raw_input("What is the temperature in degrees C? "))
    word = F_to_qualitative(better_C_to_F_2(temp_C))
    print "Hmm, it is very " + word + " today, don't you think?"

# Prompt the user for temp in C
# Make a comment like "it is warm today".
def discuss_weather_in_metric_3():
    temp_C = int(raw_input("What is the temperature in degrees C? "))
    print "Hmm, it is very " + F_to_qualitative(better_C_to_F_2(temp_C)) + " today, don't you think?"


# Prompt the user for temp in C
# Make a comment like "it is warm today".
# DO NOT TRY THIS AT HOME
def discuss_weather_in_metric_4():
    print "Hmm, it is very " + F_to_qualitative(better_C_to_F_2(int(raw_input("What is the temperature in degrees C? ")))) \
          + " today, don't you think?"

# A function with two inputs
def is_divisible(x, y):
    if (x % y == 0):
        return True
    else:
        return False

def better_is_divisible(x, y):
    return (x % y == 0)

def main():
    discuss_weather_in_metric()
    discuss_weather_in_metric()
