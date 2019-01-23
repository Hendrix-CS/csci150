# Conditionals!

import random

r = random.random()
print "The random number is", r

if (r < 0.2):
    print "Low"
elif (r >= 0.2 and r < 0.6):
    print "Medium"
elif (r >= 0.6 and r < 0.8):
    print "High-ish"
else:
    print "High"

n = random.randint(3,10)
print n

##passwd = raw_input("What is the password? ")
##if (passwd == 'swordfish'):
##    print "Here be secrets."
##else:
##    print "No secrets for you!!"
##
### Indentation determines what is inside the if!
##print "Goodbye"
