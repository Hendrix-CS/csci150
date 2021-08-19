# Repetition in Python!

# while is very similar to if

# syntax for if (review):

# if <condition>:
#   stuff

# 'stuff' gets done 0 or 1 times, depending on the <condition>.

# syntax for while:

# while <condition>:
#   stuff

# 'stuff' gets done 0 or *more* times.
# - checks the condition
# - if condition is true, does 'stuff'
# - then returns to check the condition again
# - etc, keeps doing this until the condition is false.

# Example that counts from 1 to 10:

# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1
# print('Done')
# print(count)

# count = 1
# while count <= 10:
#     count = count + 1
#     print(count-1)
# print('Done')
# print(count)

# Typical components when using a while loop:

# 1. Create/initialize a variable to control the loop
# 2. while <some condition involving the variable>:
#       do some stuff
# 3.    update the variable

# Example:
# 1. Print "hi!"
# 2. Ask the user (using input()) if they would like to quit
# 3. Stop if they type 'quit' and go back to step 1 otherwise.

# 'done' is a "sentinel"

# done = False
# while not done:
#     print("hi")
#     answer = input("Do you want to quit? ")
#     if answer == 'quit':
#         done = True
#     # else:
#     #     done = False

# Alternatively:

# answer = ''
# while answer != 'quit':
#     print("hi")
#     answer = input("Do you want to quit? ")


# Python code to explore the Collatz conjecture
#   1. Pick a starting number
#   2. If it is even, divide by 2, else multiply by 3 and add 1
#   3. Keep going until reaching 1.

limit = int(input("Test numbers up to: "))
start = 1
while start < limit:
    n = start
    count = 0
    while n != 1:        # keep looping until reaching 1
        if n % 2 == 0:   # if n is even
            n = n // 2
        else:
            n = 3*n + 1
        count = count + 1
    print(f'{start}: {count}')
    start = start + 1
