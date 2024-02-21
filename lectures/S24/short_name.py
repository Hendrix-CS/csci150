name = input("What is your name? ")

while len(name) < 5:
    print(f"The name {name} is very short.")
    name = input(f"{name}, give me a longer version of your name: ")

print(f"{name}, the loop has ended.")