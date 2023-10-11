# For loops

# Recall an example using while loops:

def explode(s: str):
    i: int = 0
    while i < len(s):
        print(s[i])
        i += 1

# This works, but it's annoying: we have to write the same code every time (i = 0; i < len(...); i += 1)
# and it's easy to get wrong.

def explode2(s: str):
    for c in s:
        print(c)

# In general,
#
# for x in s:
#   stuff
#
# executes 'stuff' once for each item in the string or list 's'.  Each time, it assigns the item to the variable x.
#
# - 'x' is a new variable
# - 's' can be any expression which will result in a string or list.
#
# In other words, it is equivalent to (and a shortcut for):
#
# i: int = 0
# while i < len(s):
#   x = s[i]
#   stuff
#   i += 1

# Example:

# count(haystack, needle) will return the number of times the character 'needle' is found in the 'haystack'.
# e.g.  count('banana', 'a') == 3.
def count(haystack: str, needle: str) -> int:
    total: int = 0
    for ch in haystack:
        if ch == needle:
            total += 1
    return total

animals: list[str] = ['tiger', 'komodo dragon', 'capybara', 'naked mole rat']

for animal in animals:
    print(f'And on this farm he had a {animal}')

for animal in animals:
    animal += 's'   # Doesn't work!

i: int = 0
while i < len(animals):
    animals[i] += 's'  # Works.
    i += 1

print(animals)

# find(haystack, needle) should return the index of the first occurrence of needle in haystack,
# or -1 if it is not found.
#
# e.g.
#   find('banana', 'a') == 1
#   find('hiccup', 'c') == 2
#   find('banana', 'z') == -1
# def find(haystack: str, needle: str) -> int:
#     for c in haystack:
#         if c == needle:
#             return ????    # Don't know what index c was located at.

# Solutions?
#   1. We could go back to using a while loop with an index variable.  =(
#   2. We could use a for loop but keep track of the index with our own variable.  =(
#   3. Use 'range'!

# find(haystack, needle) should return the index of the first occurrence of needle in haystack,
# or -1 if it is not found.
#
# e.g.
#   find('banana', 'a') == 1
#   find('hiccup', 'c') == 2
#   find('banana', 'z') == -1
def find(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i

    # If Python reaches this line, it is because it never
    # found the needle (if it had, it would have immediately
    # returned the index and not finished the loop).
    return -1

# find_all(haystack, needle) returns a list of every index
# where needle can be found in haystack. e.g.:
#
#   find_all('banana', 'a') == [1, 3, 5]
#   find_all('hiccup', 'c') == [2, 3]
#   find_all('banana', 'z') == []
def find_all(haystack: str, needle: str) -> list[int]:
    found: list[int] = []
    for i in range(len(haystack)):
        if haystack[i] == needle:
            found.append(i)

    return found

# is_sorted(nums) will tell us whether nums is in order from smallest to biggest.
#
# e.g.:
#   is_sorted([1,4,7,8]) == True
#   is_sorted([1,7,4,8]) == False
#   is_sorted([1,1,1,5,8]) == True
#   is_sorted([7]) == True
#   is_sorted([]) == True
def is_sorted(nums: list[int]) -> bool:
    ???