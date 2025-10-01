# Project #1 -- Due Today!!
# Homework #5 -- Strings, assigned today
#   - both some CodingBat and 'handwritten' work




## Looping with strings

# Often, we want to "walk across" a string,
# inspecting each character one at a time
#
# Use a while loop:

# General Structure:
#
# i = 0
# while i < len(string):
#   do whatever to your string
#   i += 1


def string_counter(s: str, char: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] == char:
            count += 1
        i += 1

    return count

## Typical loop structure:

# accum = starting value
# i = 0
# while i < len(s):
#     do things to s/accum as appropriate
#
#     i += 1
#
# return accum

def string_find(s: str, char: str) -> int:
    i = 0
    while i < len(s):
        if s[i] == char:
            return i

        i += 1

    return -1

def find_last(s: str, char: str) ->int: # should return *last* occurrence, or -1
    ind = -1

    i = 0
    while i < len(s):
        if s[i] == char:
            ind = i

        i += 1

    return ind





# Unfortunately, there is no way to change a string 'in place'
# If you want to return a manipulated value of a string
# you must build the whole string from scratch
def string_replace(s: str, old: str, new: str) -> str:
    new_str = ''
    i = 0
    while i < len(s):
        if s[i] == old:
            new_str = new_str + new
        else:
            new_str = new_str + s[i]

        i += 1

    return new_str





def reverse(s: str) -> str:
    rev = ''

    i = 0
    while i < len(s):
        rev = s[i] + rev

        i += 1


    return rev




# Write is_inorder(s: str) -- will take in a lower case word
# and return True if the characters all appear in alphabetical order
# repeated letters are ok:


# 'hiss' is True, as is 'art', but 'sleet' is False



def is_inorder(s: str) -> bool:

    i = 0
    while i < len(s) - 1:
        if s[i] > s[i + 1]:

            return False

        i += 1

    return True

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # i = 0
    # while i < len(s) - 1:
    #     # check two character -- return False if not in order
    #     if s[i] > s[i+1]:
    #         return False
    #     i += 1
    #
    # return True
    #
    #
