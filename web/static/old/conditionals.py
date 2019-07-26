# If statement (conditional)
#
# if boolean_expression:
#   stuff
#   more stuff

passwd = input("What is the password? ")
if passwd == 'dog':
    print("Secrets!!")
    print("More secrets!!")
elif passwd == 'DOG':
    print("So close!")
elif passwd > 'CAT':
    if passwd == 'ZEBRA':
        print("Zebra??")
    else:
        print("Almost!")
    print("Here")
else:
    print("WRONG")
print("Not secret")