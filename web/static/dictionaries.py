from typing import *

# Dictionary associates animals (values) with enclosure IDs (keys)
zoo1: Dict[str, str] = { 'A20': 'tapir', 'C': 'panda', 'S9': 'dragon' }
  # In general  { key: value, key: value, ... }

print(zoo1)

zoo2: Dict[str, str] = {}  # empty dictionary
zoo2['A20'] = 'tapir'      # associate a new value with the key 'A20'
zoo2['C'] = 'panda'
zoo2['S9'] = 'dragon'

print(zoo2)

print(zoo2['C'])

# Dictionary is like a function mapping keys to values.
# Consequences:

# 1. There can only be one value per unique key.

# e.g. this replaces the panda
zoo2['C'] = 'tiger'

# 2. There *can* be multiple different keys with the same value.
zoo2['F19'] = 'dragon'
zoo2['QR17'] = 'panda'
zoo2['cafeteria'] = 'potato'

zoo2['AAA'] = 'bugs'

print(zoo2)

# 3. You can look up a value by key, but not a key by value.


# Other things you can do with dictionaries:
# - Get a list of all keys with .keys()
# - Get a list of all values with .values()
# - Check if a key is present using 'in'  (if key in dict ...)
# - Get the number of keys with len(...)
# - Iterate over all the keys using for loop

# Example: frequency_count function that returns a dictionary.
# e.g.  frequency_count('hello') = {'h': 0.2, 'e' : 0.2, 'l': 0.4, 'o': 0.2}

def frequency_count(s: str) -> Dict[str, float]:

    # Step 1: make a dictionary of counts, e.g. {'h': 1, 'l': 2, ...}
    counts: Dict[str, int] = {}

    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    freqs: Dict[str, float] = {}
    for c in counts:
        freqs[c] = counts[c] / len(s)

    return freqs

# Take a dictionary of counts e.g. {'a': 1, 'c': 20, 'f': 8 ...}
# and normalize it by dividing each count by the sum of all counts
def normalize(counts: Dict[str, int]) -> Dict[str, float]:
    # Step 1: add up all the counts

    # Alternative 1 (most straightforward):

    count_sum: int = 0
    for s in counts:
        count_sum += counts[s]

    # Alternative 2 (using values() to get list of values)

    # count_sum: int = 0
    # for c in counts.values():
    #     count_sum += c

    # Alternative 3 (using built-in sum() function)

    # count_sum: int = sum(counts.values())

    # Step 2: generate the dictionary of frequencies,
    # by dividing everything by the sum

    # Alternative 1, not a good idea! Mutates the original dictionary!

    # for s in counts:
    #     counts[s] /= count_sum
    #
    # return counts

    # Alternative 2, better: make a new dictionary

    freqs: Dict[str, float] = {}
    for s in counts:
        freqs[s] = counts[s] / count_sum

    return freqs

def main():
    f = open('dictionaries.py', 'r')
    freqs = frequency_count(f.read())

    minFreq = 1
    minChar = ''
    for c in freqs:
        if freqs[c] < minFreq:
            minFreq = freqs[c]
            minChar = c
    print(minFreq)
    print(minChar)

main()
