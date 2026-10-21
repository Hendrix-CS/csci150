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
    1



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
    1
# in the string s, replace each instance of a with b
def string_replace(s: str, a: str, b: str) -> str:
    1



# notice that we can replace the string without returning
