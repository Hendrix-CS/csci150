import random

# passwd: str = input("What is the password? ")
#
# # Syntax:
# # if <any boolean expression>:
# #     indented stuff
# # else:     (optional)
# #     more indented stuff
#
# if passwd == 'opensesame':
#     print("Secrets for you!")
#     print("This is another secret.")
# else:
#     print("That is not the correct password.")
#
# print("This always happens at the end.")

# Get a random number between 0 and 1
r: float = random.random()

# if r < 0.20:
#     print("You win a car!!!!")
# else:
#     if r >= 0.20 and r < 0.40:
#         print("You win free candy!!")
#     else:
#         if r >= 0.4 and r < 0.7:
#             print("You win a sock!")
#         else:
#             print("Sorry, you don't win anything.")

# A better, equivalent way to do the above:
if r < 0.20:
    print("You win a car!!!!")
elif r >= 0.20 and r < 0.40:
    print("You win free candy!!")
elif r >= 0.4 and r < 0.7:
    print("You win a sock!")
else:
    print("Sorry, you don't win anything.")