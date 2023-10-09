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