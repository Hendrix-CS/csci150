def add3(x: int, y: int, z: int) -> int:
    return x + y + z


# print takes some value and prints it on the screen.
# print(add3(2, 5, 7))

name = input("What is your name? ")
print("Greetings, " + name + "!")


# input always returns a string!
age_str = input("What is your age? ")
# convert age_str to an int.
age = int(age_str)
print("In 20 years you will be " + str(age + 20) + "!")

# str(blah) will convert blah to a string