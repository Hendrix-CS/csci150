# Lists!

# String = sequence of characters
# List = sequence of anything.

# Lists are mutable!

# For mutating lists:
#   - list[idx] = new value
#   - list.append(new)
#   - list.pop()
#   - list.remove(element)

# Input: items (list)
# Print elements of the list, one per line.
def explode_list(items):
    n = 0
    while n < len(items):
        print(items[n])
        n += 1

animals = ['gorilla', 'dog', 'koala', 'python']

# Inputs: none
# Output: list of strings entered by the user
#
# Repeatedly prompt the user for inputs until
# they type 'quit', then return a list of all their inputs.
def read_inputs():
    answer = input("What would you like to list? ")
    stuff = []
    while answer != "quit":
        stuff.append(answer)
        answer = input("What would you like to list? ")
    return stuff
                   
def read_inputs2():
    answer = ''
    stuff = []
    while answer != "quit":
        answer = input("What would you like to list? ")
        if answer != 'quit':
            stuff.append(answer)
    return stuff
                   
    
