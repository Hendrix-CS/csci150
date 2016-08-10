
def main():
    # Building a dictionary
    animals = { 'A3' : 'tapir', 'B9' : 'alligator', 'B4' : 'frog' }

    # Alternatively:
    animals2 = {}  # empty dictionary
    animals2['A3'] = 'tapir'
    animals2['B9'] = 'alligator'
    animals2['B4'] = 'frog'

    # Get all the keys
    animals.keys()

    # Get all the values
    animals.values()

    # Check whether a key is in a dictionary using 'in'
    'C99' in animals

    # Delete a mapping from the dictionary
    del animals['B9']

    # iterate over keys with a for loop
    for k in animals2:
        print k, animals2[k]

    # note the above get printed in no particular order
    # dictionaries are unordered!


# Rewrite frequency_counts to return a dictionary mapping
# from letters to frequencies instead of a list.
#
# Input: string
# Output: dictionary mapping from letters to frequencies (between 0 and 1)

def frequency_counts(s):
    freqs = {}
    for c in s:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1

    normalize(freqs)
    return freqs

# Input: dictionary with numbers as values
# Modify the input dictionary: divide all values in the dictionary by the total.
def normalize(d):
    total = 0
    for k in d:
        total += d[k]

    # Alternative:
    # for v in d.values():
    #    total += v

    for k in d:
        d[k] /= float(total)

# Input: dictionary with frequency counts as values
# Output: key, chosen at random according to the frequency counts
def probable_choice(freqs)
