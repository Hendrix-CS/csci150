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

# Return True if the list of strings contains the given string.
# e.g.  contains(['hi', 'there', '150'], 'there') == True
# e.g.  contains(['hi', 'there', '150'], 'book') == False
# e.g.  contains(['hi', 'there', '150'], 'HI') == False
def contains(haystack: list[str], needle: str) -> bool:

    for word in haystack:
        if word == needle:
            return True

    # Looked through entire list without finding the needle, so
    # return False
    return False


def contains2(haystack: list[str], needle: str) -> bool:
    seen: bool = False
    for word in haystack:
        if word == needle:
            seen = True

    return seen

# What if we wanted a for loop to count from 0 to 9?
# Can we use a for loop?

for i in range(10):    # range(n) counts from 0 to n-1
    print(i)

# Can use this to do the same thing some number of times
for _ in range(23):
    print('hello')

# We can use this to count through every index in a list or string.
for i in range(len(animals)):
    print(f'And on this farm he had animal #{i}: {animals[i]}')

# Return the index of the needle in the haystack, or -1 if it is not found.
def find_index(haystack: list[str], needle: str) -> int:
    # Does not work: we don't know what index to return!
    # for word in haystack:
    #     if word == needle:
    #         ????

    for i in range(len(haystack)):   # Loop through all valid indices of the list
        if haystack[i] == needle:
            return i

    return -1

# Check whether the numbers are in order smallest -> biggest
def is_sorted(nums: list[int]) -> bool:
    # Idea: look through every pair of consecutive items in the list,
    # see if they are in order.

    # Only loop to one before the end since we want to check each item and the next.
    for i in range(len(nums) - 1):
        # If the current item is greater than the next item, the list is out of order
        if nums[i] > nums[i+1]:
            return False

    # If we got through the whole list and never found two items out of order, the list is in order
    return True