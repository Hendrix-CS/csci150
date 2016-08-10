from random import *

r = random()
passwd = raw_input("Enter the password: ")
if (r < 0.2):
    print "You got heads!"
elif (r >= 0.2 and r < 0.6):
    print "You got tails!"
else:
    print "You got pickles!"
    if (passwd == "pass"):
        print "Here be secrets"
    else:
        print "No secrets for you"
