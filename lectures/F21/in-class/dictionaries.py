# Dictionaries

# Consider the list ['tapir', 'ferret', 'anteater']

# we can also think of this as a "mapping" from indices to
# animal names:
#
# 0 -> 'tapir'
# 1 -> 'ferret'
# 2 -> 'anteater'
#
# We can think of the numbers 0,1,2 as "keys" that we can
# use to look up the corresponding animal name.  However,
# we're limited to using consecutive numbers starting at 0.
#
# What if we want to have other kinds of "keys"? e.g.
#
# 'K14' -> 'tapir'
# 'ZZ25' -> 'ferret'
# 'Q' -> 'anteater'
#
# We can do this with dictionaries.

from typing import *

# We write dictionaries using curly braces.
# We can list each key ("index") along with its
# corresponding value.
zoo = {'K14': 'tapir', 'ZZ25': 'ferret', 'Q': 'anteater'}

# We can look up the value corresponding to a given key
# by writing  zoo[key]

# {} is an empty dictionary.
# We can start with an empty dictionary and add keys & values
# to it one at a time.
zoo2 = {}
zoo2['K14'] = 'tapir'

# Dictionaries can only have one value per key.
# (if you want multiple values for one key, you could store
# a list).
# But multiple keys could have the same value.
# You can only look up a value by key, not vice versa.

# A few other things we can do with dictionaries:
#   1. Get list of all keys with .keys()
#   2. Get list of all values with .values()
#   3. Ask for the number of key/value pairs with len()
#   4. Iterate over all the keys using a for loop.

for enclosure in zoo:
    print(f"There is a {zoo[enclosure]} in enclosure {enclosure}.")

# Example: a function to compute the frequency count of
# each character in a string.  It will return a dictionary
# associating each character to the number of times
# that character appeared.
#
# For example,
#
# frequency_counts('banana!') =
#   { 'b' : 1, 'a' : 3, 'n' : 2, '!' : 1 }

# Dict[str,int] means a dictionary with str keys
# and int values.
def frequency_counts(s: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for c in s:
        if c in counts: # check if c is already a key in
                        # the dictionary
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

# Alternative definition:
def frequency_counts2(s: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts

# Normalize a dictionary of counts by dividing each count
# by the total.
#   e.g. normalize({'a': 2, 'b': 5, 'c': 3})
#      = {'a': 0.2, 'b': 0.5, 'c': 0.3}
def normalize(counts: Dict[str,int]) -> Dict[str,float]:

    # First, compute the total count by adding up
    # all the individual counts
    total: int = 0
    for key in counts:
        total += counts[key]

    # Now, compute the frequency for each character
    # by dividing the count of that character
    # by the total count.
    freqs: Dict[str, float] = {}
    for key in counts:
        freqs[key] = counts[key] / total

    return freqs

# Given a file name, compute the frequencies of all
# characters that occur in the file.
#
# e.g. file_freqs('dictionaries.py') = {'a': ....}
def file_freqs(file_name: str) -> Dict[str, float]:
    file = open(file_name, 'r')
    contents: str = file.read()
    file.close()
    return normalize(frequency_counts(contents))

def file_word_freqs(file_name: str) -> Dict[str, float]:
    file = open(file_name, 'r')
    words: List[str] = []
    for line in file.readlines():
        words += line.strip().split()
    file.close()
    return normalize(frequency_counts(words))
