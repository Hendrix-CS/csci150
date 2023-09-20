# While loops!

# Recall if statements:
#
# if <condition>:
#    stuff
#    more stuff
#
# Stuff inside the if is executed either 0 or 1 times.

# While loop looks like this:
#
# while <condition>:
#    stuff
#    more stuff
#
# Stuff inside the while is executed 0 or 1 or 2 or 3 or ... times.
# After doing the stuff, we return to check the condition again, and keep
# doing this until the condition is false.

x = 0          # 1. Create a variable with an initial value that will control the loop.
while x < 5:   # 2. Condition that mentions the variable.
    print(x)   # 3. Some stuff that you want to happen repeatedly.
    x = x + 1  # 4. Update the variable as the last thing in the loop.

print('Done!')
