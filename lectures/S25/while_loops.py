# 1. Print "hi"
# 2. Ask the user if they want to quit
# 3. If they type "quit", stop, otherwise go back to step 1.

go = True
while go:
    print("hi")
    stop = input("Would you like to quit? (y/n) ")
    if stop == "y":
        go = False

done = False
while not done:
    print("hi")
    stop = input("Would you like to quit? (y/n) ")
    if stop == "y":
        done = True

quit = 'n'
while quit != 'y':
    print("hi")
    quit = input("Do you want to quit? (y/n) ")