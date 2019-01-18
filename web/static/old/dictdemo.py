from typing import *

animals = ['marsupial', 'mollusk', 'bird']

# A way to think about this: each item has an index:
#
# 0 -> 'marsupial'
# 1 -> 'mollusk'
# 2 -> 'bird'
#
# We say the indices are "keys" which "map to" the string values.

# Dictionaries are similar, but the "keys" can be any values, not just
# numbers from 0..n-1.

# For example, mapping habitat codes to animals:
#
# 'A20' -> 'marsupial'
# 'B19' -> 'mollusk'
# 'Sub-basement' -> 'bird'

# Lists use square brackets, dictionaries use curly braces.

habitats = {'A20': 'marsupial', 'B19': 'mollusk', 'Sub-basement': 'bird'}

habitats2 = {}
habitats2['A20'] = 'marsupial'
habitats2['B19'] = 'mollusk'
habitats2['Sub-basement'] = 'bird'
habitats2['C27'] = 'mollusk'

# Note there can be only one value for each key (i.e. keys are unique).
#   (but the value could be a list).
# But there can be multiple keys with the same value.
# We can only look up values by key, not keys by value.

# Things to do with dictionaries

# Get a list of all keys with .keys(), or values with .values()

habitatKeys = habitats2.keys()
habitatValues = habitats2.values()

# Check if a key is contained in a dictionary using 'in'

bool1 = 'A20' in habitats2
bool2 = 'F9999' in habitats2

# Delete a key with 'del'

del habitats2['A20']

# Iterate over the keys with for

for h in habitats2:
    print(h + " houses " + habitats2[h])



# Example: a better frequency_count!

# Input: some text
# Output: a dictionary mapping each character in the text
#   to the number of times it occurs.
def frequency_count(text: str) -> Dict[str, int]:
    letter_dict = {}
    for c in text:
        if c not in letter_dict:
            letter_dict[c] = 0
        letter_dict[c] += 1
    return letter_dict


# Input: a dictionary of counts
# Output: a new dictionary obtained by dividing each of the counts
#   by the total.
#
# e.g. normalize({'h': 1, 'e': 1, 'l': 2, 'o': 1})
#   = {'h': 0.2, 'e': 0.2, 'l': 0.4, 'o': 0.2}
def normalize(counts: Dict[str, int]) -> Dict[str, float]:
    normalized = {}
    # total = 0
    # for c in counts:
    #     total += counts[c]
    total = sum(counts.values())
    for i in counts:
        normalized[i] = counts[i]/total
    return normalized

##############################################################
# File I/O (Input/Output)

## Writing to a file:

# 1. "Open" a file
f = open("example.txt", "w")   # "w" = writing mode

# 2. Write to it
f.write("Hello!!\n")
f.write("CSCI 150!!\n")

# 3. Close it
f.close()

## Reading from a file:

# 1. Open it
f = open("dictdemo.py", "r")  # "r" = reading mode

# s = f.read()  # Entire contents as a giant string

ls = f.readlines()  # Get the lines of the file as a list
total_words = 0

for l in ls:
    total_words += len(l.split())

# 3. Close it
f.close()

print("dictdemo.py contains " + str(total_words) + " \"words\".")