# Reminders
# Project #2 Due Friday
# -- Friday's class is a Demo day -- we'll play each other's word games
# -- requests for extensions must be submitted by class time on Friday

# But what about:
#
# given a list of ints, return True if they are in increasing order, False otherwise

def is_sorted(lst: list[int]) -> bool:
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False
        i += 1
    return True

# Can we do this with a for loop?

# Yes -- we'll start there on Wednesday

def is_sorted_for(lst: list[int]) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True




# The construction:

# i = 0
#
# while i < len(lst):
#
#
#     i += 1

# can be replicated by

# for i in range(len(lst)):

# So if you need explicit access to the indices for any reason, you can either:
# -- use a while loop, as we have been doing
# -- use range()

# while loops are nice, but you can mess up the "infrastructure"
# range() is (maybe) simpler to write, but you need to think carefully about what
#      goes in the parentheses

# a few rules about using for loops in general:
# -- you should *never*, *never*, *never* change the length of iterable object itself in a for loop
# -- you cannot easily use a for loop to replicate a sentinel while loop
#         that is, when you have an initially indefinite number of loops to do



# lists vs strings
# recall that strings are immutable -- you cannot adjust a string 'in place'

# you can change the value of an item in a list
# but list *are* mutable

# in the list of ints lst, replace each even int with 1/2 of that number
def lst_even(lst: list[int]) -> list[int]:

    # this version changes the original list as well
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2

    #return lst



    # this version, creates a *new* list, and leaves original alone
    # return_lst = []
    # for item in lst:
    #     if item % 2 == 0:
    #         return_lst.append(item // 2)
    #     else:
    #         return_lst.append(item)
    #
    # return return_lst


    # this version does not work
    # since item is not literally the object in the list
    # it does not affect lst at all

    # for item in lst:
    #     if item % 2 == 0:
    #         item = item // 2
    # return lst

# for strings, we cannot reassign a value at an index:
# that is, the construction
# s[i] = new_letter
# does not work.

# of our three attempts at replacing (some) values in the list above,
# only mimicking the first one turns out to work
def str_replace_before_m(s: str) -> str:
    t = ''
    for char in s:
        if char < 'm':
            t += 'z'
        else:
            t += char

    return t



