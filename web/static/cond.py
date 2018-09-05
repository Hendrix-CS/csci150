# bool type: True, False
# boolean operators: not, and, or
# comparison operators: == (equal), != (not equal), <, >, <=, >=

# Conditional statements!
#
# if <condition>:
#     statement1
#     statement2
#     ...
# <more statements>

# x = int(input("Enter a number: "))
#
# if x < 10:
#     print("That is a small number.")
#     print("***********************")
# print("Thank you for entering the number " + str(x) + ".")

# if <condition>:
#     statements
# else:
#     other statements

import random

r = random.random()
if r < 0.1:
    print("Wow, you are unlucky!")
    print("Try again next time.")
else:
    print("Yay! You get a prize!")
    if r > 0.9:
        print("You get a car!!!11")
    else:
        if r > 0.7:
            print("You get a bike!")
        else:
            if r > 0.5:
                print("You get a book!")
            else:
                if r > 0.3:
                    print("You get a sock!")
                else:
                    print("You get a stick of gum!")

# The above sucks
# Here's a better way to write the same thing:

r = random.random()
if r < 0.1:
    print("Wow, you are unlucky!")
    print("Try again next time.")
else:
    print("Yay! You get a prize!")
    if r > 0.9:
        print("You get a car!!!11")
    elif r > 0.7:
        print("You get a bike!")
    elif r > 0.5:
        print("You get a book!")
    elif r > 0.3:
        print("You get a sock!")
    else:
        print("You get a stick of gum!")

