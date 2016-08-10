# 16 March 2016
# Dictionaries

# Dictionaries are a generalization of lists:
#   - lists map consecutive indices to values
#   - dictionaries map arbitrary 'keys' to values.

animal_list = ['tapir', 'crocodile', 'wombat']

# map habitats to animals
#   'A23' -> 'tapir'
#   'B19' -> 'crocodile'
#   'B12' -> 'wombat'

animal_dict = { 'A23' : 'tapir', 'B19' : 'crocodile', 'B12' : 'wombat' }

# Look up value in a dictionary using syntax
#
#   dict[key]

animal_dict2 = {}  # empty dictionary
animal_dict2['A23'] = 'tapir'
animal_dict2['B19'] = 'crocodile'
# etc.

# Other things we can do with dictionaries:
# - Get a list of all the keys with .keys()
# - Get a list of all the values with .values()
# - Check if a key is in the dictionary using 'in'
# - Get the number of keys with len()
# - Delete a key/value pair with 'del'
#     e.g.  del dict[key]
# - Loop over the keys using 'for'

# Example: frequency count

# Input: string
# Output: dictionary, keys are characters, value d[k]
#   is number of occurrences of k in input string.
def counts(s):
    count_dict = {}
    for c in s:
        if c not in count_dict:
            count_dict[c] = 1
        else:
            count_dict[c] += 1
    return count_dict

# Alternate implementation:
def counts2(s):
    count_dict = {}
    for c in s:
        if c not in count_dict:
            count_dict[c] = 0

        count_dict[c] += 1
    return count_dict

# Input: dictionary with ints or floats as values
# Output: normalized dictionary --- each value is
#    is divided by sum of all the values.
def normalize_dict(d):
    total = 0
    for k in d:
        total += d[k]
    # total = sum(d.values())

    for k in d:
        d[k] = d[k] / float(total)

    return d
