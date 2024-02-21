name = input("What is your name? ")
age = int(input("What is your age? "))
pay = float(input("What is your hourly wage? "))

if age < 18:
    print(f"{name}, I hope you are in school.")
elif age < 65:
    print(f"{name}, I hope you are gainfully employed.")
else:
    print(f"{name}, I hope you are enjoying a well-deserved retirement.")