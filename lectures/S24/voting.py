name = input("Your name? ")
birth_year = int(input(f"What year were you born, {name}? "))
current_year = int(input("What year is it now? "))

age = current_year - birth_year
if age < 18:
    print(f"Sorry {name}, you are not eligible to vote quite yet.")
elif current_year % 4 == 0:
    print(f"{name}, you can vote for President this year!")
elif current_year % 4 == 2:
    print(f"{name}, you can vote for Arkansas governor this year!")
else:
    print("Sorry, no governor or president this year.")
