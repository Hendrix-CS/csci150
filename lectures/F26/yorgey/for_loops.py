def explode(s: str):
    i = 0
    while i < len(s):
        c = s[i]
        print(c)
        i += 1

# We've seen code like this many times, but there are lot of ways we could
# get this wrong:
#
#   1. use <= instead of <
#   2. put i += 1 outside the loop (or forget it entirely)
#   3. start i at wrong index
#   etc.

# There is a better way, using a 'for loop'!

def explode_for(s: str):
    for c in s:    # Loop through every character in s...
        print(c)   # ...and print it

# Also works for lists!

animals: list[str] = ['goose', 'eel', 'whale shark', 'capybara', 'chinchilla']
for animal in animals:
    print(f'And on this farm he had a {animal}! EIEIO!')

# In general:
#
# for <new variable> in <thing>:
#   do stuff with <new variable>
#
# This will repeat once for each item in <thing>.  Each item will be assigned to <new variable>.
#
# <thing> can be a string or a list, or other stuff we will see later.

# Examples!

# count how many times 'needle' occurs in 'haystack'.
# e.g.  count('banana', 'n') == 2
#       count ('banana', 'z') == 0
def count(haystack: str, needle: str) -> int:
    # idea: loop through each character in 'haystack'
    # check if it is equal to 'needle', increment count

    count = 0
    for c in haystack:
        if c == needle:
            count += 1

    return count

# Return a list of only the strings of length 5 or more.
def filter_long(strs: list[str]) -> list[str]:
    result: list[str] = []
    for s in strs:
        if len(s) >= 5:
            result.append(s)

    return result