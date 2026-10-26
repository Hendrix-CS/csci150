# Recall, a list is a sequence of values; each value has an *index*.

#             0           1           2          3
animals = ['ferret', 'alligator', 'anteater', 'skunk']

# We can also think of this as a *mapping* or *association* from indices to values.
#
#  0 --> 'ferret'
#  1 --> 'alligator'
#  2 --> 'anteater'
#  3 --> 'skunk'

# A dictionary generalizes this to be able to use any values we want as "indices" (*keys*).
# For example, associating animals to exhibit ID codes:

# 'A2' --> 'ferret'
# 'QQ9' --> 'alligator'
# 'Z3' --> 'anteater'
# 'F' --> 'skunk'

# One way to create a dictionary with explicit keys and values:

zoo = {'A2': 'ferret', 'QQ9': 'alligator', 'Z3': 'anteater', 'F': 'skunk'}

# We can look up the value associated with a particular key using the same syntax
# we use to look up an index in a list:

a = zoo['Z3']   # look up the value associated with 'Z3' (== 'anteater')

# We can modify the value associated with a key:

zoo['Z3'] = 'tiger'

# We can also add new keys and values this way:

zoo['R19'] = 'anteater'

# Note each key can only occur once, but there can be multiple keys with the same value:

zoo['T12'] = 'anteater'


### Example: frequency count function

# Return a frequency count of a string, i.e. a dictionary whose keys are characters and associated values are
# how many times each character occurred.
#
# e.g.
#   frequency_count('apple') = {'a': 1, 'p': 2, 'l': 1, 'e': 1}

def frequency_count(s: str) -> dict[str, int]:   # dict[str, int] means keys are str, values are int.
    counts: dict[str, int] = {}   # start off with an empty dictionary

    # Loop through each character c of the string s
    for c in s:
        if c not in counts:
            counts[c] = 0

        counts[c] += 1

        # OR:
        # if c not in counts:
        #     counts[c] = 1
        # else:
        #     counts[c] += 1

    return counts