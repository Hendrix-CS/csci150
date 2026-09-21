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
    while count >= 0:
        print(f'Hello {count}')
        count = count + 1

hellos_loop()

# Common pattern with while loops:
#
# 1. create a variable to control the loop
# 2. while (something with variable):
#      *do some stuff*
#      3. update the variable as the last step in the loop