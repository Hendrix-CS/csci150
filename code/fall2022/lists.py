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
    list = []
    while user_input != "quit":
        list.append(user_input)
        user_input = input("Enter a string: ")
    return list

print(read_inputs())