# Functions!

# Functions can be defined in any order --- put them in whatever order
# makes the most sense / helps you best communicate how the program works or
# what it is doing.

# From now on, all the code we write must be in functions!  Only exception
# is a call to main() at the very end.

# Python functions might not need any input, and might not return a value as output.
def main():
    response = input("OK? ")
    print("Hello!")
    z = add(3,6)
    print(z)
    print_greeting()
    print("Done!")

# Variables defined in a function are *local*, that is,
# they can only be accessed inside that function.
def add(x: int, y: int) -> int:
    z = x + y
    q = 3
    return z

def print_greeting():
    name = get_name()
    print(f"Greetings, {name}!")

def get_name() -> str:
    q = 3 / 0
    return input('What is your name? ')

main()