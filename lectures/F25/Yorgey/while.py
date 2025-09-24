# While loops!

# while <condition>:
#   do stuff

# like an if, but can run any number of times, not just once.

# - If <condition> is false, skip the while loop and move on (just like an 'if').
# - If <condition> is true, do the stuff in the loop and then return to the
#   beginning of the loop and check the condition again, etc.

# 1. Initialize some variable to control the loop.
count = 0

# 2. While loop with a condition that mentions the variable.
while count < 10:
    print(count)

    # 3. Last thing in the loop updates the variable.
    count = count + 1


# Example: add up all the numbers from 1 to 100.
count = 1
sum = 0
while count <= 100:
    sum = sum + count    # OR   sum += count
    count = count + 1    # OR   count += 1
print(sum)

def sum_up_to(n: int) -> int:
    count = 1
    sum = 0
    while count <= n:
        sum = sum + count  # OR   sum += count
        count = count + 1  # OR   count += 1
    return sum