
# Repetition in Python!

# while <condition>:
#   stuff1
#   stuff2
#   ...

# if executes 0 or 1 time
# while executes any number of times (zero or more)

# Example

# count = 0
# while count < 10:
#     print(count)
#     count = count + 1

# Common components of using a while loop:
#
# 1. Create a variable to control the loop. (count = 0)
# 2. Write the while with a condition that mentions the variable.
# 3. Do some stuff in the loop
# 4. The last statement in the loop updates the variable. (count = count + 1)


# Write a program which prints "Hello", then asks the user whether they want to quit.
# If the user types "yes", the program stops, otherwise it starts over.

# Method 1
# quit = input("Hello! Would you like to quit? ")
# while quit != "yes":
#     quit = input("Hello! Would you like to quit? ")

# Method 2
# print("Hello!")
# quit = input("Do you want to quit? ")
# while quit != "yes":
#     quit = input("Do you want to quit? ")

# Method 3
# quit = False
# while quit == False:
#     print("Hello!")
#     i_wanna_die = input("Do you want to quit? ")
#     if i_wanna_die == 'yes':
#         quit = True

# Method 4
quit = 'no'
while quit != "yes":
    quit = input("Hello! Do you want to quit? ")

