# While loops!

# while loops are actually similar to if statements:
#
# if <condition>:
#   stuff that should only happen if <condition> is true
#   more stuff
#
# while <condition>:
#   stuff that should only happen if <condition> is true
#   more stuff
#
# When the while <condition> is true, it does the stuff inside
# *and then goes back to the top and checks the condition again*
#
# In other words, the content of an if statement happens 0 or 1 times.
# The content of a while loop happens 0 or more times.

# Typical features of a while loop:

# 1. Initialize some variable to control the loop.
count = 0
sum = 0

# 2. While condition that mentions the variable.
while count < 10:

    # 3. Stuff that you want to repeat
    print(count)

    sum = sum + count

    # 4. Very last thing in the loop: update the loop control variable.
    count = count + 1

print(f'The sum of 0..9 is: {sum}')

