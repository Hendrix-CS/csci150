name = input("What is your name? ")
age = int(input("What is your age? "))
work_start = int(input("What was your age when you started working? "))
pay = float(input("What is your annual pay? "))
retirement_share = float(input("What fraction of your income goes to retirement? "))
retirement_goal = float(input("How much money do you want to have at retirement? "))

years_worked = age - work_start
retirement_savings = years_worked * pay * retirement_share

print(f"{name}, you have saved ${retirement_savings:.2f} for retirement.")

still_need = retirement_goal - retirement_savings
still_expected = (65 - age) * pay * retirement_share

if still_need < 0:
    print(f"{name}, congratulations, you are ready to retire right now!")
elif still_expected >= still_need:
    print(f"{name}, you are not yet ready to retire, but you are on track.")
else:
    print(f"{name}, I am sorry to tell you that you are ${(still_need - still_expected):.2f} short.")
