from typing import *
# Consider the following two similar pieces of code:

############ Code Part 1
# def function1(x: int):
#     x += 1
#     return x
#
#
# def main1():
#     x = 5
#     print(x)
#     y = function1(x)
#     print(x)
#     print(y)
#
#
# main1()
#
#
#
#
############## Code Part 2
# def function2(a: List[int]):
#     a.append(7)
#     return a
#
#
# def main2():
#     a = [9, 2, 5, 11]
#     print(a)
#     b = function2(a)
#     print(a)
#     print(b)
#
#
# main2()

# What happened?

# In Python, mutable object variable (lists for us so far, but there are others) are defined by
# *references* rather than by single values stored

# For example:

# x = 139
# y = x
# x = x - 200
#
# print(x)
# print(y)

# y will still have the value of 139. When Python reads the 'y = x' line the variable
# y is not linked in any particular way to x. It simply takes on the value that x currently has
# if x or y later have their values changed, that does not affect the other one.

# List work differently.
# When you create a list and assign it to a variable, say a = [9, 2, 5, 11]
# the list is created and variable name a "points" to this list.
# If any other variable, say b, is assigned to match a, then they both
# reference the same list!!

#a= [9, 2, 5, 11]
#b = a

# Anything done to a (or to b) affect the other!
#b[2] = 999
#print(a)

# This is *very* weird, and hard to get used to. We will use the "heap" to track this:
# All functions running share the heap -- which means that all of them can access, but also change
# the values of objects in the heap!

# Let's return to

# def function2(a: List[int]):
#     a.append(7)
#     #return a
#
#
# def main2():
#     a = [9, 2, 5, 11]
#     function2(a) # notice that this time, we are not even returning anything!!!
#     print(a)
#
#
# main2()

# We can fix this:

# If you want to copy the value of a list to another, you can use:

# a = [9, 2, 5, 11]
#b = a[:]

# Now, a and b have the same value currently, but are not linked.

# a[2] = 9999
# print(a)
# print(b)

# Formally, what is really going on here is that all variables are really about memory locations
#
#
# (I explain a bit about memory addresses here - you are not responsible in anyway for this
#  Take CSCI 151 - Data Structures if you are interested)


### The Heap
# Mutable Objects (lists for now, though we'll have one other type after Break)
# always go in the Heap, not the Function Stack.
# Variables which point to objects in the Heap are essentially sharing them
# Change something in the Heap, and you have changed it for *all* variables which point to it!!

# Simple Heap Tracing Examples -- The solution is posted on the class website as well

#1)

# def main():
#     lst = [5, 2, 3]
#     mst = lst
#     new_lst = []
#     for item in lst:
#         new_lst.append(item)
#
#     lst[1] = 17
#     mst.append(-10)
#     new_lst.append(94)
#
#     print(lst)
#     print(mst)
#     print(new_lst)
#
# main()



#2)
#
# def fun1(n: int, my_list: List[int]) -> int:
#     i = 7
#     while len(my_list) < n:
#         my_list.append(i * 2)
#         i += 1
#     return i
#
#
#
# def main2():
#     x = 6
#     y = x
#     y += 5
#
#     lst = [7, 8, -2]
#
#     y = fun1(x, lst)
#
#     print(x)
#     print(y)
#     print(lst)
#
#
#
#
# main2()
#
#
# #Have a great Spring Break.

