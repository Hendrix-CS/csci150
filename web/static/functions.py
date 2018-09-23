# Functions
#
# Examples we've seen:
#
#   - print(...)  takes one thing as input and prints it on the screen
#   - input(...)  takes a string as input, prompts the user, and returns as output whatever they type.

# We can make our own functions!


# Say hi two times.
def say_hi_twice():
    say_hi()
    say_hi()

# Greets the user, asks their name, and ignores it.
def say_hi():   # inputs go in the parentheses
    print("Hello there CSCI 150!")
    print("This is a function.")
    input("What is your name? ")
    print("Whatever.")
    print(5/0)

def say_hi_a_lot():
    say_hi_twice()
    say_hi()
    say_hi_twice()

def even_more_hi():
    say_hi_a_lot()
    say_hi_a_lot()

# say_hi_twice()

# Take a temperature in degrees C as input, and print a message with
# the temperature converted to F.
def C_to_F_message(temp_C: float):
    temp_F: float = temp_C * 9/5 + 32
    print("The temperature in degrees Fahrenheit is " + str(temp_F) + "°F.")

# Interactively prompt the user for a temperature in degrees C and print a message
# with the temp converted to F.
def C_to_F_interactive():
    temp_C: float = float(input("What is the temperature in degrees C? "))
    C_to_F_message(temp_C)
    print("Have a nice day!")

# temp_F is a *local variable*: only defined inside the function.

# Better version of C_to_F which does only *one* job (converting C -> F).
# Take a temp in degrees C as a parameter, and return the temp in degrees F.
def C_to_F(temp_C: float) -> float:
    # temp_F: float = temp_C * 9/5 + 32
    # return temp_F

    # Alternatively:
    return temp_C * 9/5 + 32

# Convert a temperature in degrees F to a descriptive adjective.
def F_to_qualitative(temp_F: float) -> str:
    if temp_F < 0:
        return "frigid"
    elif temp_F <= 32:
        return "freezing"
    elif temp_F <= 50:
        return "cold"
    elif temp_F <= 75:
        return "nice"
    elif temp_F <= 90:
        return "warm"
    elif temp_F <= 110:
        return "hot"
    elif temp_F <= 150:
        return "blazing"
    else:
        return "dead"

# Prompt the user for the temperature in degrees C and make an appropriate comment
def discuss_weather():
    temp_C: float = float(input("What is the temperature in degrees C? "))
    temp_F: float = C_to_F(temp_C)
    word: str = F_to_qualitative(temp_F)
    print("My, it's very " + word + " today, don't you think?")

discuss_weather()

# Prompt the user for the temperature in degrees C and make an appropriate comment
def discuss_weather2():
    print("My, it's very " + F_to_qualitative(C_to_F(float(input("What is the temperature in degrees C? ")))) + " today, don't you think?")
