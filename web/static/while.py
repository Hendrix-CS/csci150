# While loops!

# Syntax:
#
# while <condition>:
#   <stuff>
#
# This will keep doing <stuff> as long as <condition> is true.

# 1. Create some variable to control the loop (before the loop)
n: int = 1

# 2. Loop itself with a condition involving the variable
while n < 10:
    print(n)

    # 3. Update/change the variable (often @ the end of the loop)
    n = n + 1

print("Done!")

# - print "hi"
# - ask the user if they want to quit
# - repeat until the user types 'yes'.

# q: str = "no"
# while q != "yes":
#     print("hi")
#     q = input("Do you want to quit? ")

# print("hi")
# q: str = input("Do you want to quit? ")
# while q != "yes":
#     print("hi")
#     q = input("Do you want to quit? ")

# print("hi")
# while input("Do you want to quit? ") != "yes":
#     print("hi")

done: bool = False
while not done:
    q: str = input("Hi! Do you want to quit? ")
    if q == "yes":
        done = True