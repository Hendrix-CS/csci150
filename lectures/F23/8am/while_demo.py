# While loops!

# Remember if statements:
#
# if <condition>:
#    stuff
#    more stuff
#
# Stuff inside the if is executed 0 or 1 times.

# While loops:
#
# while <condition>:
#    stuff
#    more stuff
#
# Stuff inside the while is executed 0 or 1 or 2 or 3 ... or any number of times.

# 1. Initialize a variable to control the loop.
n = 1
while n <= 10:   # 2. Some condition that mentions the variable from step 1
    print(n)     # 3. Do some stuff that we want to repeat
    n = n + 1    # 4. Last: update the variable.

print("Done!")