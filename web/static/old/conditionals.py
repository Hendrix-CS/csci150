# CSCI 150
# January 30, 2017
# Conditionals

import random

r = random.random()   # random float in [0,1)

if r < 0.2:
    print("r is small")
elif r >= 0.2 and r <= 0.6:   # elif = "else if"
    print("r is mediumish")
elif r < 0.8:
    print("r is biggish")
else:
    print("r is big")

##password = input("Please type the password: ")
##
### password is passw0rd123
##
##if password == "passw0rd123":
##    print("Here be secrets")
##    print("Even more secrets")
##else:
##    print("No secrets for you!")
##
##print("Goodbye")