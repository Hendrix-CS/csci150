
# Project #2 due Wednesday
# - I am available:
#      - Friday 10am - 3pm
#      - Monday 10am - 3pm
#      - Tuesday 9:45am - 12 noon, 1-3pm
#  You can also ask questions over the weekend -- but:
#   - If you want to show me any code, use a Teams chat
#   - Send code, not pictures/screenshots
#   - Ask one or more specific questions:
#         - My get_level() function  does not work - it does not return the right value when I type 'easy'
#         - The play_again() function never lets me play again
#     NOT: "Can you look over my code?" or "The whole thing doesn't work."
#        - I am happy to do those in person today/next week


# Consider the following two similar pieces of code:

############ Code Part 1
def function1(x: int) -> int:
    x += 1
    return x

def main1():
    x = 5
    print(x)
    y = function1(x)
    print(x)
    print(y)

#main1()

############# Code Part 2
def function2(c: list[int]) -> list[int]:
    c.append(7)
    return c

def main2():
    a = [9, 2, 5, 11]
    print(a)
    b = function2(a)
    print(a)
    print(b)
#
#main2()

# What happened?

# In Python, mutable object variables (lists for us so far, but there are others)
# are defined by  *references* rather than by single values stored
#
# (it is more complicated than this, but this will do for now)

# For example:

# x = 139
# y = x
# x = x - 200
#
# print(x)
# print(y)

# y will still have the value of 139. When Python reads the 'y = x' line the variable
# y is not linked in any particular way to x.
# It simply takes on the value that x currently has
# if x or y later have their values changed, that does not affect the other one.

# List work differently.
# When you create a list and assign it to a variable, say a = [9, 2, 5, 11]
# the list is created and variable name a "points" to this list.
# If any other variable, say b, is assigned to match a, then they both
# reference the same list!!

# a= [9, 2, 5, 11]
# b = a

#Anything done to a (or to b) affect the other!
# b[2] = 999
# print(a)

# This is *very* weird, and hard to get used to. We will use the "heap" to track this:
# All functions running share the heap
# -- which means that all of them can access, but also change
# the values of objects in the heap!

# Let's return to
#
# def function2(x: List[int]):
#     x.append(7)
#     return a


# def main2():
#     a = [9, 2, 5, 11]
#     function2(a) # notice that this time, we are not even returning anything!!!
#     print(a)
# #
# #
#main2()

# We can fix this:

# If you want to copy the value of a list to another, you can use:

# a = [9, 2, 5, 11]


# b = a[:]
#
#
# # Now, a and b have the same value currently, but are not linked.
#
# a[2] = 9999
# print(a)
# print(b)

# Formally, what is really going on here is that all variables
# are really about memory locations
#
#
# (I explain a bit about memory addresses here
# - you are not responsible in any way for this
#  Take CSCI 151 - Data Structures if you are interested)

def id_check():
    a = 0
    b = 0

    while id(a) == id(b):
        a += 1
        b += 1

    print(a,id(a),b,id(b))

def id_check_str():
    a = ''
    b = ''

    while id(a) == id(b):
        a += 'a'
        b += 'a'

    print(a,id(a),b,id(b))




