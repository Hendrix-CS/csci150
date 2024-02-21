name = input("What is your name? ")

num_letters = len(name)
if num_letters <= 4:
    print(f"{name} is very short.")
elif num_letters >= 10:
    print(f"{name} is very long.")
else:
    print(f"{name} is of a typical length.")
