# 24 Feb 2016
# CSCI 150
# Lists!

# Lists are sequences of anything!
# Just like strings are sequences of characters.

# The empty list is written []
# len( )  works on lists too.
# Write lists using [x, y, ...] notation.

# You *can* have things of different type in a list,
#   but DON'T.

# Lists are indexed just like strings.

# +, *, len( ), all work on lists just like for strings.

# range(n) is the list of ints from 0 to n-1.

# Strings are *immutable*, lists are *mutable*.
# Methods for modifying lists:
#   - append(elt)  --- add elt to the end of the list.
#   - pop(index)    --- remove something at an index.
#   - remove(elt)  --- remove the given element
# del list[index]   --- same as list.pop(index)
# del list[slice]     --- remove a whole slice

# Inputs: none
# Output: a list of strings entered by the user
#
# Repeatedly prompt user for inputs until they type
# 'quit', then return a list of all inputs.
def read_inputs():
    inputs = []
    done = False
    while not done:
        word = raw_input('Enter another input, or quit: ')
        if word.lower() == 'quit':
            done = True
        else:
            inputs.append(word)

    return inputs
