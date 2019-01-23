# 15 Feb 2017
# Repeeettttitttinonnnn!!!!

# Basic repetition in Python: "while loop".

# Like an if: if = 0 or 1 times, while = 0 or more times.

# while <condition>:
#    <body>

# Keeps executing <body> as long as <condition> is true.

n = 0
while n < 10:
    print(n)
    n = n + 1  # increment n   (or  n += 1)

# Common/key aspects of while loops:
# 1. Create and initialize control variable
# 2. Condition using control variable
# 3. Update the control variable inside the loop (usually @ end)

# Example 2:
# Print 'hi', then ask the user if they want to stop
# Stop if they type 'yes', otherwise repeat

# Create control variable:
user = 'no'
while user != 'yes':   # Condition
    print("Hi!")
    user = input("Do you want to stop? ")  # Update control var

# Approach #2: use sentinel (true/false) as control var
done = False
while not done:
    print("Hi!")
    user = input("Do you want to step? ")
    # if user == 'yes':
     #   done = True
    # else:                    # Redundant
    #   done = False

    # Alternatively:
    done = (user == 'yes')
