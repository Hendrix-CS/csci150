# For loops!

# Motivation:

def explode(s: str):
    i: int = 0
    while i < len(s):
        print(s[i])
        i += 1

# The above code is annoying: lots to get wrong, and we actually don't care
# about the indices, only about the characters in the string.


def explode2(s: str):
    for c in s:
        print(c)


animals: list[str] = ["cow", "giraffe", "anteater", "bear", "ant"]
for animal in animals:
    print(f"And on this farm he had a {animal}, EIEIO")

# In general:
#
# for <new variable> in <list or string expression>:
#   ... stuff using <new variable> ...
#   ... etc ...
#
# The loop will execute a number of times equal to the length of the list or string
# <new variable> will be assigned to each element of the list / character of the string.
#
# Think of
#
# for var in list:
#    do stuff
#
# as an abbreviation for
#
# i: int = 0
# while i < len(list):
#   var = list[i]
#   do stuff
#   i += 1
#
#

# For loop doesn't execute at all if the list/string is empty:
nums: list[int] = []
for n in nums:
    print(n/0)
print("done")

nums2: list[int] = [2,5,6,9]
s: int = 0
for n in nums2:
    if n % 2 == 0:
        s += n
print(f"The sum is {s}.")


# Count how many times needle occurs in haystack.
# e.g.  count('banana', 'n') == 2
def count(haystack: str, needle: str) -> int:
    num_occurrences: int = 0
    for letter in haystack:
        if letter == needle:
            num_occurrences += 1
    return num_occurrences

# Return a new list with only the strings of length 5 or more
# e.g.  filter_long(["hi", "there", "xyz", "abcdefg"]) == ["there", "abcdefg"]
def filter_long(strs: list[str]) -> list[str]:
    new_list: list[str] = []
    for long_string in strs:
        if len(long_string) >= 5:
            new_list.append(long_string)

    return new_list