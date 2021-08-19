# Lists!

# A list is a sequence of any values, just like a string
# is a sequence of characters.

# A list with three ints
exampleList = [18, 29, -5]

# A list with four strs
exampleList2 = ["hello", "there", "CSCI", "150"]

# A list of lists of booleans
exampleList3 = [[True, False], [False], [True, True, True]]

# Elements in a list are indexed from 0,
# we can retrieve them by writing list[index], just like
# with strings.
#
# Many things work the same with lists and strings:
#   - indexing
#   - concatenation (+) : glue two lists into one longer list
#   - len()
#   - list * n  glues n copies of the list together

# - range(n) gives the list [0, 1, 2, ... n-1]
# - [] is the empty list of length 0

# String values can't be changed (strings are *immutable*)
#   we can only replace an old string in a variable
#   with a new one
# However, lists can be changed (lists are *mutable*).

animals = ['cat', 'dog', 'lizard']
animals[1] = 'lemur'
print(animals)

animals.append('horse')   # Add one new element to the end
                          # of a list
print(animals)

# You can also look up  list.pop(index), list.remove(element)

# x: int = 5
#
# myList = [15, x + 3, 7*x + 2, 9] # works fine!
# print(myList)

# Python let us do this:
weird_list = [3, False, "hello", ['pig', 7.2]]
# All the items have different types.
# But this is a terrible idea and you should never do this!
# The items in a list should always be all the same type.

from typing import *

# Given the above import, instead of  l: list  we can write
# e.g. l: List[int].

# Add up all the numbers in a list and return their sum.
# e.g.  sum_list([1,9,17]) = 27
#       sum_list([5,-5,5,-5]) = 0
def sum_list(nums: List[int]) -> int:
    i: int = 0
    sum_so_far: int = 0
    while i < len(nums):
        sum_so_far += nums[i]
        i += 1
    return sum_so_far

# Repeatedly prompt the user for an input until they type
# 'quit'.  Then return the list of all the inputs the
# user typed (not including the final 'quit').
def read_inputs() -> List[str]:
    done: bool = False
    user_inputs: List[str] = []
    while not done:
        user: str = input("Please enter an input: ")
        if user == 'quit':
            done = True
        else:
            user_inputs.append(user)

    return user_inputs

# Strings vs lists

# To convert a string into a list of characters:
#   - list(str) turns the string into a list
#   - str.split() splits a string into pieces.
#
# >>> "banana".split("n")
# ['ba', 'a', 'a']
# >>> "This is a sentence of words".split(" ")
# ['This', 'is', 'a', 'sentence', 'of', 'words']
# >>> "This    is a   sentence    with  spaces".split()
# ['This', 'is', 'a', 'sentence', 'with', 'spaces']
#
# - To turn a list of strings/characters back into a single
#   string, use  delimiter.join(list)
#
# >>> steps = ['dog', 'cog', 'cot', 'cat']
# >>> ' -> '.join(steps)
# 'dog -> cog -> cot -> cat'
# >>> ' '.join(['This', 'is', 'a', 'sentence.'])
# 'This is a sentence.'
# >>> ''.join(steps)
# 'dogcogcotcat'

# >>> print('Hello\nworld')
# Hello
# world
# >>> print("Hello\\nworld")
# Hello\nworld
# >>> '\n'.join(['This is a line.', 'next line', 'third line'])
# 'This is a line.\nnext line\nthird line'
# >>> print('\n'.join(['This is a line.', 'next line', 'third line']))
# This is a line.
# next line
# third line

animals: List[str] = ['stingray', 'horse', 'llama', 'frog']
# goal: add three gerbils to the end
# i.e. ['stingray', ...., 'gerbil', 'gerbil', 'gerbil']

# Does not work: adds a single list of three things to the end
#   instead of adding three things.
# animals.append(['gerbil', 'gerbil', 'gerbil'])

# Works!
# count: int = 0
# while count < 3:
#     animals.append('gerbil')
#     count += 1

# Doesn't work --- doesn't change animals
# gerbil_list = ['gerbil']
# animals + gerbil_list * 3

# Works!
gerbil_list = ['gerbil']
animals = animals + gerbil_list * 3


## Example list functions

# Find the product of a list of numbers
def prod_list(nums: List[int]) -> int:
    i: int = 0
    prod_so_far: int = 1
    while i < len(nums):
        prod_so_far *= nums[i]
        i += 1
    return prod_so_far

# Find the maximum value in a non-empty list of numbers
#
# e.g.  max_list([2,7,3]) = 7
#       max_list([2,2,2,2]) = 2
#       max_list([217]) = 217
def max_list(nums: List[int]) -> int:
    i: int = 1
    max_so_far: int = nums[0]
    while i < len(nums):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
        i += 1
    return max_so_far


# This version works for lists of *nonnegative* ints
#   but it doesn't work if we give it all negative numbers!
# def max_list(nums: List[int]) -> int:
#     i: int = 0
#     max_so_far: int = 0
#     while i < len(nums):
#         if nums[i] > max_so_far:
#             max_so_far = nums[i]
#         i += 1
#     return max_so_far

# Return a new list which contains only the even
# numbers from the input.
#
# e.g. onlyevens([1,5,6,2,3,7,8]) = [6,2,8]
#      onlyevens([1,7,3]) = []

def onlyevens(nums: List[int]) -> List[int]:
    i: int = 0
    evens: List[int] = []
    while i < len(nums):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
        i += 1
    return evens