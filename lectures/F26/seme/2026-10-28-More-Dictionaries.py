# Reminders
# Quiz Friday -- For Loops
# Final Project
#   -- start to think about what you might do: I am happy to help you brainstorm
#   -- design document due Monday, November 16
#   -- Project Due (& Demo Day) Friday, December 11 (9am)

# Dictionaries, part ii

# A matching between a *key* and a *value*

test_dict = {'a': 5, 'b' : 7, 'c': -2, 'd': 5, 'e': 11}

# You can directly loop over the keys:

# for k in dictionary:

def print_keys(d: dict[str, int]):
    for k in d:
        print(k)

# To get the values:

def print_values(d: dict[str, int]):
    for k in d:
        print(d[k])


# Given a dictionary with string keys and integer values, return the sum of all values

def sum_values(d: dict[str, int]) -> int:
    total = 0
    for k in d:
        total += d[k]

    return total

# we can easily check if a particular key is in a dictionary:

# 'b' in test_dict
# 'z' in test_dict

# It is harder to check if a value is there

def value_in(d: dict[str, int], n: int) -> bool:
    # look through dictionary, one entry at a time
    # is the current value == n?  If so, return True
    # keep going
    #if we make it to the end and still haven't found n, return False

    for k in d:
        if d[k] == n:
            return True
    return False

# What about creating a dictionary?
# Given a string, return a dictionary with individual characters as keys and their frequency as value

def str_freq(s: str) -> dict[str, int]:
    alpha = 'abcdefghijklmnopqrtuvwxyz'
    freq_dict = {}
    for char in alpha:
        freq_dict[char] = 0

    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1

    return freq_dict

# we will do more of this type on Friday


