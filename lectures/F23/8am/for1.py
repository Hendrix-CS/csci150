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