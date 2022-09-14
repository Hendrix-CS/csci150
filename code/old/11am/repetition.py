## if bool:
##     stuff

#n = 1
#while n <= 10:
#    print(n)
#    n += 1
#    n = n + 1

## Initialize some variable
## while bool related to the variable:
##     stuff, which has the opportunity to
##     change the variable

# The program will keep printing "hi" and
# asking "do you want to stop?" If they say
# yes, stop the loop, otherwise repeat.

def first():
    n = 1
    while n == 1:
        print("hi")
        c = input("Do you want to stop1? ")
        if c == "yes":
            n = 2
#        else:
#            n = 1

def second():
    greetings = "no"
    while greetings != "yes":
        print("hi")
        greetings = input("Do you want to stop2? ")

def third():
    print("hi")
    n = "hi"
    while n == "hi":
        t = input("Do you want to stop3? ")
        if t == "yes":
            n = "no"
        else:
            print("hi")

def fourth():
    print("hi")
    while (input("Do you want to stop4? ") != "yes"):
        print("hi")

def fifth():
    while True:
        print("hi")
        if input("Do you want to stop5? ") == "yes":
            break

def sixth():
    done = False
    while not done:
        print("hi")
        if input("Do you want to stop6? ") == "yes":
            done = True

sixth()
