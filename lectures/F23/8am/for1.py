# For loops!

# Recall examples like this:

def explode(s: str):
    i: int = 0
    while i < len(s):
        print(s[i])
        i += 1

# This works but it kind of sucks --- lots of tedious code to repeat, lots of things to get wrong.
# Python has 'for loops' which allow us to do the same thing but in a much nicer way.

def explode2(s: str):
    for c in s:
        print(c)

# In general:
#
# for x in s:
#   stuff using x
#   more stuff
#   etc.
#
# Executes the 'stuff' once for each item in the string or list s
# Each item is assigned to x one at a time.
#
# Equivalent to:
#
# i: int = 0
# while i < len(s):
#   x = s[i]
#   stuff
#   i += 1

# Works with lists too!
animals: list[str] = ['dodo', 'naked mole rat', 'alligator', 'nutria']
# animals.sort()

for animal in animals:
    print(f'And on this farm he had a {animal}')

for animal in animals:
    print('Adding s...')
    animal += 's'    # Doesn't work since we are only changing a copy of the strings in the list,
                     # not the list itself.

i: int = 0
while i < len(animals):
    animals[i] += 's'
    i += 1

print(animals)

# count(haystack, c) counts how many times c occurs in haystack.
def count(haystack: str, needle: str) -> int:
    total: int = 0
    for c in haystack:
        if c == needle:
            total += 1
    return total

# Given a list of strings, return a new list which excludes all the long strings (len >= 25)
def filter_long(msgs: list[str]) -> list[str]:
    new_msgs: list[str] = []
    for msg in msgs:
        if len(msg) < 25:
            new_msgs.append(msg)
    return new_msgs

# find(haystack, needle) should return the index of the first occurrence of needle in haystack,
# or -1 if it is not found.
#
# e.g.
#    find('banana', 'a') == 1
#    find('Good morning CSCI 150', 'C') == 13
#    find('banana', 'z') == -1
# def find(haystack: str, needle: str) -> int:
#     for c in haystack:
#         if c == needle:
#             return ???

# problem --- how do we know what index to return?
# Potential solutions:
#   1. Go back to using a while loop with an index variable =(
#   2. Keep using a for loop but keep track of an index variable too. =(
#   3. Use a for loop over a range!

# find(haystack, needle) should return the index of the first occurrence of needle in haystack,
# or -1 if it is not found.
#
# e.g.
#    find('banana', 'a') == 1
#    find('Good morning CSCI 150', 'C') == 13
#    find('banana', 'z') == -1
def find(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i  # return immediately: we found it!

    # If it makes it all the way through the for loop,
    # it means it never found the needle (since if it had,
    # it would have returned and never reached this line).
    return -1

# find_all(haystack, needle) should return a list of all indices where needle
# occurs in haystack.
#
# e.g.
#   find_all('banana', 'a') == [1, 3, 5]
#   find_all('Good morning CSCI 150', 'C') == [13, 15]
#   find_all('banana', 'z') == []
def find_all(haystack: str, needle: str) -> list[int]:
    found: list[int] = []
    for i in range(len(haystack)):
        if haystack[i] == needle:
            found.append(i)

    return found

# is_sorted should check whether the list is sorted in order from smallest to biggest.
#
# e.g.
#   is_sorted([1,3,7,12]) == True
#   is_sorted([1,1,1,2,3]) == True
#   is_sorted([1,2,1]) == False
#   is_sorted([20,7,3]) == False
#   is_sorted([]) == True
#   is_sorted([5]) == True
def is_sorted(nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False

    return True