# More functions!
#
# From now on, *all* the code we write will be in functions! Like so:

# Function definitions can be in whatever order makes sense!

def main():
    print("Do some stuff")
    response = input("OK? ")
    z = add(2,3)   # this is OK even though add is defined below
    print(z)
    print_greeting()
    print("Done!")

def add(x: int, y: int) -> int:
    return x + y

# Notice this function does not take any inputs nor return any output; its job is just to do stuff.
def print_greeting():
    name = get_name()    # Every function call must have parentheses after it!
    print(f'Greetings, {name}!')  # We cannot use the variable 'name' from the get_name function
                                  # since variables are *local*, i.e. a variable only exists inside
                                  # the function where it is created.

# Ask the user to input their name, and return it.
def get_name() -> str:
    name = input("What is your name? ")
    z = 3 / 0
    return name

main()