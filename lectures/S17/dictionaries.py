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






