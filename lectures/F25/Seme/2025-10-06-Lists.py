
# Quiz Friday on Strings



from typing import *

# we can make other ordered collections:

#my_list: List[int] = [7, 3, 4, 7, 2]
#
## # Type declarations: Though not required above, this is how we let a
# # human reader (and Pycharm) know
# # to expect my_list to be a list of integers.
# # You ***MUST** have the "from typing import *" line above for this to work
#
# # Compare:
#
#'dog->dot->lot->let'
#
#sol_list: List[str] = ['dog','dot','lot','let']
#
#

#
#
#
# # the items in a list go inside [square brackets] and are separated by commas
#
# #print(type(my_list))
#
# # the individual entries in a list can be anything:
#
#other_list = [4, 6, 'a', '6', True, [6,'abc'],3.14159]
#
# # but you really shouldn't do this. Python itself does not care,
# # but you will make mistakes -- this is hard for a human to conceptualize
# # and you'll need to spend a lot of time remembering that entry 4 is
# # a boolean, while entry 5 is a list of
# # half ints and half strings....
#
# # Basic list construction/manipulation:
#
# # the empty list:
#lst = []



#
# # indices -- work just like strings:
#
my_list = [7, 3, 4, 7, 2]
#
# print(my_list[1])
# print(my_list[1:4])
# print(my_list[1:2])
# print(my_list[1:1])
# #
# # print(my_list[1:4])
#
# #the 'in' operation:
# print(4 in my_list)
# # #
# print(10 in my_list)
#
# # (in works for strings as well --)
# print()
# print()
#
# print('s' in 'my_string')
# print('x' in 'my_string')
# print('rn' in 'my_string')

# print(3 in [[3],5,7,8])
# print([3,5] in [4, 7,[3,5],7,8])
#
#print([1,2,3] == [1,3,2])
#
# # In many ways, lists and strings are similar
# # There is a fundamental difference, though:
#
# # Strings are immutable -- when you make a string, it is fixed
# # and cannot be changed.
#
# # Lists are mutable. You can change individual entries:
#my_list = [7, 2, 3, 5, 7]
#print(my_list)
#
# my_list[1] = 1234
# #
# print(my_list)
# # # #
# s = 'my_string'
# print(s)
# s[4] = 'g'
# print(s)
#

x = 5
y = x
x = x + 1
# print(x)
# print(y)





# Complication -- we will talk about this later this semester
# a = [1, 2, 3]
# b = a
# a[1] = 5
# print(a)
# print(b)

## Operations on lists
# We can add elements to a list with append()
my_list = [7, 2, 3, 5, 7]
# my_list.append(1234)
# print(my_list)
#
# # Append always adds to the end.
#
# # You can add two lists:
#
# print([1,2,3] + [7,5,3])
# # #
# # # # You can multiply a list by a non-negative integer:
# print([1,2,3] * 4)
# #
# # # #Length
# print(my_list)
# print(len(my_list))
# #
# print(len([[3, 5], 7, 8]))


# List operations:
#pop() -- removes from the list by index *and* returns that value
my_list = [7,2,7,8,1]
# print(my_list)
#x = my_list.pop(10)
# print(my_list)
# print(x)
#
# # remove() - removes by *value* and does not return anything -- only removes the first occurrence
# my_list.remove(6)
# print(my_list)

#split() - given a string and a character (or sequence of characters), returns a list, split on the character.
# string1 = 'hi there how are you today?'
# print(string1.split(' '))
# #print(string1.split(' h'))
# print(string1.split('z'))

# join() -- the opposite of split:  str.join(list) will return a string with a the value of str between each entry
# only works if the original list is made up of string entries

print(';'.join(['Hi','there','how','are','you?']))
#
lst = ['dog','log','lot','tot']
print('->'.join(lst))

my_list = [4, 6, 7, 10, 1]

def sum_list(lst: List[int]) -> int:
    s = 0
    i = 0
    while i < len(lst):
        s += lst[i]

        i += 1

    return s

print(my_list)
print(sum_list(my_list))


