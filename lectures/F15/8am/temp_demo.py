##C = float(raw_input("What is the temp in degrees C? "))
##F = 1.8*C + 32
##print "The temp in degrees F is " + str(F)
##

# this function is poorly designed
def C_to_F(temp_C):    # temp_C is a *parameter*
    F = 1.8*temp_C + 32
    print "The temp in degrees F is " + str(F)

def say_hi_twice():
    say_hi()
    say_hi()

def say_hi():   # header
    print "Hello CSCI 150!"    # body
    print "We are learning about functions!"

# say_hi_twice()

# Why use functions?
  # saves repetition of lots of code
  # break program up into smaller pieces for testing
  # enables code reuse


# Better -- only computes the temp conversion
def C_to_F(temp_C):    # temp_C is a *parameter*
    F = 1.8*temp_C + 32    # convert C to F
    return F               # ... then tell us the result

    # "Fruitful function"  or just  "function"

def C_to_F_alt(temp_C):    
    return 1.8*temp_C + 32      # this does the same thing

def C_to_F_weird(temp_C):    
    F = 1.8*temp_C + 32  
    return F
    print "The temperature is", F    # this never happens

def C_to_F_weird(temp_C):    
    F = 1.8*temp_C + 32
    print "The temperature is", F   # this does happen
    return F


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
      
def is_divisible(x, y):
    return x % y == 0

def greet():
    temp_C = float(raw_input("What is the temperature in degrees C? "))
    print "It is " + F_to_qualitative( C_to_F(temp_C) ) + " today."

def greet2():
    greet()
    greet()

