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







    
