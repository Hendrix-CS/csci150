# For loops

# Common pattern:

animals = ["chicken", "rat", "stingray", "cow"]

# i: int = 0
# while i < len(animals):
#     print(animals[i])
#     i += 1

# Above works, but it's annoying because:
#   - Have to make variable i
#   - Have to get the test (< len) right
#   - Have to remember to update i
#   - etc.

# Better way:

for a in animals:
    print(a)

# In general:

# for <new variable> in <list expression>:
#    ... do stuff with variable ...

# Also works for strings:

# for c in "hello":
#     print(c)
#
# for c in "hello":
#     print(c)
#     if c < 'i':
#         print("!!!")

print(animals)

for a in animals:
    a = a + "!"

print(a)
print(animals)

for a in '':     # Does nothing!
    print(10/0)

# Count how many times c occurs in s
# e.g. count('banana', 'n') = 2
def count(s: str, c: str) -> int:

    num_occurrences: int = 0
    for a in s:
        if a == c:
            num_occurrences += 1

    return num_occurrences

from typing import *

# Return a list containing only the elements with len >= 5
# e.g. filter_long(["hi", "there", "xy", "abcdefgh"]) = ["there", "abcdefgh"]
def filter_long(things: List[str]) -> List[str]:
    pass