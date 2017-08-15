# Dictionaries

# Recall lists:

animals = ['koala', 'dingo', 'aardvark', 'hyena']

# This is a sequence, but we can also think of it like this:

# keys -> values
# 0 -> 'koala'
# 1 -> 'dingo'
# 2 -> 'aardvark'
# 3 -> 'hyena'

# Dictionary is the generalization that lets us associate
# values to *arbitrary* keys, not just consecutive integers.

# Example: associate animals to habitats.

# 'A20' -> 'koala'
# 'B6' -> 'dingo'
# 'S12' -> 'aardvark'
# 'BASEMENT' -> 'hyena'

zoo = { 'A20' : 'koala', 'B6' : 'dingo', 'S12' : 'aardvark'
           , 'BASEMENT' : 'hyena' }
# Note the order is irrelevant!

# We can look up the value associated to a given key with
#   dict[key]
# We can associate a value to a new key, or replace the value
#   of an existing key with
#   dict[key] = value

# Empty dictionary is  {}

# Example!

# Input: string s
# Output: dictionary mapping each character to the number
#   of times that character occurs in s.
#
# Example: if s is "banana!!",
# we should get { 'a': 3, 'b' : 1, 'n': 2, '!': 2 }.

def frequency_counts(s):
    counts = {}
    for c in s:
        # If we haven't seen c before:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

# Input: dictionary d that maps characters to ints
#   (i.e. the keys are characters and the values are ints)
#   (each int is the number of times that character occurs)
#
# Output: another dictionary that maps the same
#   characters to float values.
#
# Does not modify the input dictionary.
#
# Returns a new dictionary with the same keys as the input
# dictionary, and where the values have been divided by
# the total total of all the counts.
#
# Example: {'a': 1, 'b': 3}  --->  {'a': 0.25, 'b': 0.75}
def normalize_frequencies(d):
    total = total_values(d)
    freqs = {}
    for char in d:
        freqs[char] = d[char] / total
    return freqs

# This version works, but it changes the input dictionary ---
# which is generally a bad idea.
#
##def normalize_frequencies(d):
##    total = total_values(d)
##    for char in d:
##        d[char] /= total
##    return d

# Input: a dictionary with ints as values
# Output: the total of all the values
#
# Example: {'a': 1, 'b': 3}  -->  4
def total_values(d):
    total = 0
    for char in d:
        total += d[char]
    return total

# Input: string s
# Output: dictionary mapping each character in s to
#   its frequency in s (float from 0-1).
# Example: "babb" --> {'a': 0.25, 'b': 0.75}
def frequencies(s):
    return normalize_frequencies(frequency_counts(s))



