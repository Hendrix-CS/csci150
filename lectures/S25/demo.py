# RETURN GOOD - more modular, does one simple job,
# other code can decide what to do with the result.
def f2cR(degrees_f: float) -> float:
    return (degrees_f - 32) * 5/9

# PRINT BAD (unless that's specifically what you want)
# Less modular, does too much stuff all at once,
# nothing can be done with the result once it is printed
# on the screen.
def f2cP(degrees_f: float):
    print((degrees_f - 32) * 5/9)

def greet():
    name: str = input("What is your name? ")
    # print("Hello, " + name + "!")
    # Alternative:
    print(f"Hello, {name}!")
    age: int = int(input("What is your age? "))
    if age < 25:
        print("Wow, so young!")
    else:
        print("Geez, so old!")

    temp: float = float(input("Enter a temperature in Fahrenheit: "))
    print(f"{temp}F = {f2cP(temp)}C")

greet()