# Today: repetition!

# "while loop" is similar to an if statement.
# if statement executes 0 or 1 times.
# while loop executes 0 or more times.

n: int = 0
while n < 10:
    print(n)
    # n = n + 1
    n += 1    # shorthand for  n = n + 1

# typical pattern for a while loop:
# 1. initialize a variable to control the loop
# 2. write a loop using that variable for its condition
# 3. update the variable as the last thing in the loop

# Another example:
# - print "hi"
# - ask the user if they want to stop  (use input("Do you want to stop? "))
# - keep repeating until they say "yes"

# Approach #1
user_input: str = "no"
while user_input != "yes":
    print("hi!")
    user_input = input("Do you want to stop? ")

# Approach #2: sentinel loop
wants_to_stop: bool = False   # "sentinel variable"
while not wants_to_stop:
    print("hi!")
    user_input = input("Do you want to stop? ")
    if user_input == "yes":
        wants_to_stop = True

