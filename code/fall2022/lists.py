# Lists!

# A list is a sequence of data of any type, just like a string is a sequence
# of characters.

# We can write a list using square brackets with elements separated by commas.
# e.g. [1,2,5]
#      []   -- empty list

# Python allows different type elements in a list, e.g.
#   [1, 'hi', False, [2, 3, 5]]
# but you should never do this!

# By default Python reports the type of a list to be 'list'
# But we want to know the type of the elements.

from typing import *  # We need this to say e.g.  List[int]

my_list: List[str] = ['dog', 'cat', 'chinchilla', 'unicorn', 'pegasus']

# We can get the element at an index of a list, get a slice, get the len(...)
# and concatenate lists with +, all just like strings.

# strings are *immutable*, e.g.
#   name: str = 'Sam'
#   name[2] = 'l'    # error!!!

# But lists are mutable.
my_list[1] = 'tiger'   # Replace the thing at index 1 with 'tiger'


# We can also add one element to the end of a list using  .append(element), e.g.

my_list.append('rooster')


# Let's write some example functions on lists.

# Add all the elements of the list.
#   e.g.  sum_list([2,5,3]) == 10
def sum_list(nums: List[int]) -> int:
    count: int = 0     # keep track of current index in list
    sum: int = 0       # keep track of current sum
    while count < len(nums):
        sum += nums[count]
        count += 1
    return sum

# Repeatedly prompt the user for inputs until they type 'quit', then
# return a list of all the inputs (excluding 'quit').
def read_inputs() -> List[str]:
    user_input = input("Enter a string: ")
    list: List[str] = []
    while user_input != "quit":
        list.append(user_input)
        user_input = input("Enter a string: ")
    return list

# print(read_inputs())

# More stuff with lists

# We can use the 'in' operator to test whether something is an element of
# a list or not.

print(3 in [1,2,3,4,5])
print(7 in [1,2,3,4,5])
print('n' in 'banana')

# Strings and lists

# Convert a string to a list of characters using list(...)

print("hello")
print(list("hello"))

# We can use .split(separator) to split a string into chunks

animal_str = "dog,cat,horse,fly,prairie dog"
print(animal_str.split(','))

sentence = "Hi     there, CSCI   150!"
print(sentence.split(' '))
print(sentence.split())     # splits on multiple spaces

# Turning a list into a string --- using 'join'
# separator.join(list)   --- glues all the strings in 'list' into one big string
#    with 'separator' in between each.

steps = ['dog', 'cog', 'cot', 'cat']
greeting = ["hi", "there", "CSCI", "150"]
print('->'.join(steps))
print(' '.join(greeting))
print(''.join(greeting))
print('\n'.join(greeting))

# More example functions with lists

# Find the product of the list of integers.
#   e.g.  prod_list([2,5,3]) == 30
def prod_list(nums: List[int]) -> int:
    count: int = 0     # keep track of current index in list
    prod: int = 1       # keep track of current prod
    while count < len(nums):
        prod *= nums[count]
        count += 1
    return prod

print(prod_list([2,5,3]))
print(prod_list([]))

# Count how many integers in 'lst' are smaller than 'n'.
#   e.g.  small_count([1,5,8,2,88,3,6], 7) == 5    (5 elements in the list are < 7).
def small_count(lst: List[int], n: int) -> int:
    i: int = 0          # keep track of current index in list
    count: int = 0       # keep track of current count
    while i < len(lst):
        if lst[i] < n:
            count += 1
        i += 1
    return count


print(small_count([1,5,8,2,88,3,6], 7))
print(small_count([1,5,8,2,88,3,6], 0))

# Given a list of strings which are all lowercase letters, test whether
# the list is in alphabetical order.
#
#   e.g.   alpha_order(['cat', 'dog', 'horse', 'platypus']) == True
#   e.g.   alpha_order(['cat', 'dog', 'zebra', 'horse', 'platypus']) == False
def alpha_order(lst: List[str]) -> bool:
    i: int = 0
    while i < len(lst)-1:
        if lst[i] > lst[i+1]:
            return False
        i += 1
    return True

print(alpha_order(['cat', 'dog', 'horse', 'platypus']))
print(alpha_order(['cat', 'dog', 'zebra', 'horse', 'platypus']))
