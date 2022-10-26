from typing import *

# Recall the type of a list was written
#   List[x]   where x is the type of the elements.

# The type of a dictionary is written
#   Dict[k, v]   where k is the type of the keys, and v is the type of the values.


# frequency_counts(s) returns a dictionary with characters as keys where
# each character is associated to an integer count.
#
# e.g. frequency_counts('APPLE!') == {'A': 1, 'P': 2, 'L': 1, 'E': 1, '!': 1}
def frequency_counts(s: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}      # initialize empty dictionary
    
    for c in s:      # loop through every character in the string
        if c not in counts:     # Check whether c exists as a key in the counts dictionary
            counts[c] = 0       # Add c as a key with value 0 if it wasn't there before

        counts[c] = counts[c] + 1     # Increment the count for character c
                                      # Alternatively, counts[c] += 1

    return counts