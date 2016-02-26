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

animals = ['skua', 'killer whale', 'spider', 'orangutan', 'goat']

# Ways to add 3 gerbils to the end of the list

# Doesn't quite work:
# animals.append('gerbil ' * 3)

# Runtime error:
# animals.append('gerbil') * 3

# Works!
# while len(animals) < 8:
#    animals.append('gerbil')

# Runtime error (too many arguments to append):
# animals.append('gerbil', 'gerbil', 'gerbil')

# Works!
# animals.append('gerbil')
# animals.append('gerbil')
# animals.append('gerbil')

# Same as 'gerbil' * 3
# animals.append('gerbil' + 'gerbil' + 'gerbil')

# Doesn't change animals
# animals + ['gerbil', 'gerbil', 'gerbil']

# Works!
# animals = animals + ['gerbil', 'gerbil', 'gerbil']

# Works!
# gerbil_list = ['gerbil']
# animals = animals + gerbil_list * 3

# Almost works but not quite.
# animals.append(['gerbil'] * 3)

#############################
## Lists and strings

# Strings and lists of characters are not the same!

# Converting string -> list:
#   - list(...)
#   - s.split(...)  : splits a string s into a list of strings

# Converting list -> string:
#   - glue.join(list)   # opposite of split

#############################
## Mutability, objects, and aliasing

nums = [1,2,3]
nums2 = nums
del nums[1]
print nums2

# The above code prints [1,3]! Weird!

# Variables don't contain values.
# Variables contain *references* to *objects* which have values.

# So the above code creates num and nums2 which both hold a reference
# to the same list object.  Changing one of them affects both.
