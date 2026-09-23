# 5 elements of computation:
#   input
#   output
#   arithmetic
#   conditionals
#   repetition

def hellos():
    print('Hello')
    print('Hello')
    print('Hello')
    print('Hello')
    print('Hello')
    print('Hello')

# hellos()

# How can we tell Python to repeat this 6 times instead of literally copy-pasting the code?

# Using a *while loop*:
#
# while <condition>:
#   *stuff*
#
# * An if statement does *stuff* zero or one time, depending on the condition.
# * A while loop does *stuff* zero or more times, as long as the condition is true.
#
# If the <condition> is true, Python does *stuff*, AND THEN goes back to check the condition again, etc.

def hellos_loop():
    count = 0
    while count < 6:
        print(f'Hello {count}')
        count = count + 1

# hellos_loop()

# Common pattern with while loops:
#
# 1. create a variable to control the loop
# 2. while (something with variable):
#      *do some stuff*
#      3. update the variable as the last step in the loop

# add_up_to(n) returns the sum 1 + 2 + 3 + .... + n.
def add_up_to(n: int) -> int:
    sum: int = 0    # ': int' optional, tells PyCharm what type of values we intend to store in sum

    count: int = 1
    while count <= n:
        sum = sum + count

        count = count + 1

    return sum

# Add up all the odd numbers 1 + 3 + 5 + .... up to n.
# e.g.  add_odds(5) should be   1 + 3 + 5.
def add_odds(n: int) -> int:
    sum: int = 0

    count: int = 1
    while count <= n:
        sum = sum + count

        count = count + 2

    return sum

def add_odds2(n: int) -> int:
    sum: int = 0

    count: int = 1
    while count <= n:
        if count % 2 == 1:
            sum = sum + count

        count = count + 1

    return sum

# Prompt the user to enter numbers, keep adding them up until the user enters 0
def add_numbers() -> int:
    sum: int = 0

    done: bool = False   # A boolean variable to control the loop
    while not done:
        n = int(input('Please enter a number (0 to stop): '))
        if n == 0:
            done = True
        else:
            sum = sum + n

    return sum