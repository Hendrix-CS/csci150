# Repetition in Python: while loops!

# syntax:
#
# while <condition>:
#   statement1
#   statement2
#   ...

# Executes the statements in the body repeatedly until <condition> becomes false.

# Example: print all the numbers from 1-10, each on a separate line.

n: int = 1

while n <= 10:
    print(n)
    n += 1   # abbreviation for n = n + 1

# Three usual components of a while loop:
#
# 1. Create a variable to control the loop & set an initial value.
# 2. Write a condition involving the variable
# 3. Update the variable (usually @ very end of the loop)

# Challenge: write a program which asks the user if they want to quit.
# If the user types 'quit', it quits, otherwise it asks them again.

# Method 1:
#
# answer: str = ''
#
# while answer != 'quit':
#     answer = input("Do you want to quit? ")
# print("OK, quitter!")

# Method 2:

done: bool = False

while not done:
    answer: str = input("Do you want to quit? ")
    if answer == 'quit':
        done = True
print("OK, quitter!")
