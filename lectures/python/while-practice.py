# From now on:
#    - Everything goes in a function, except possibly
#      a single call to main() at the very end.
#    - Every function should be documented.
#      - 3 things: inputs, output, description.

# Inputs:
#   - prompt: string to be used as a prompt.
# Output: int typed by the user
#
# Repeatedly prompts the user until the enter an int.
def int_input(prompt):
    valid_input = False
    while valid_input == False:
    # while not valid_input:
        user_input = raw_input(prompt)
        valid_input = user_input.isdigit() or\
                      (user_input[0] == '-' and user_input[1:].isdigit())
        if not valid_input:
            print "That's not an int, try again!"
    return int(user_input)

import time

# Inputs:
#   - n: int, starting number for the countdown
# Output: none
#
# Prints a countdown from n to 0.
def countdown(n):
    while n > 0:
        print str(n) + "..."
        time.sleep(1)
        # n = n - 1      # decrement
        n -= 1

        # In general  n @= x   means   n = n @ x
    print "BLASTOFF!!!"


    
