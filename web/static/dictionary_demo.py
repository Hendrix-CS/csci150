from typing import *

# A list maps natural numbers 0, 1, 2, ... to values.
#
# 0 -> 'alligator'
# 1 -> 'panda'
# 2 -> 'yeti'
animals : List[str]
animals = ['alligator', 'panda', 'yeti']

# A dictionary maps *arbitrary* 'keys' to values.
#
# 'B12' -> 'alligator'
# 'B14' -> 'panda'
# 'S2'  -> 'yeti'

# Dict[key type, value type]
zoo : Dict[str, str]
zoo = {'B12': 'alligator', 'B14': 'panda', 'S2': 'yeti', 'A19': 'alligator'}
# Can have multiple keys with the same value
# But only one value for a given key.
# (Like the vertical line test.)

print(zoo)

print(zoo['B14'])   # Look up the value associated with a key

zoo['B14'] = 'tiger'   # replace the value associated with a key

print(zoo)

zoo['G99'] = 'pandoc'  # add a new key & associated value

print(zoo)

# Get all the keys
print(list(zoo.keys()))

# Get all the values
print(list(zoo.values()))

# Loop once for each key in the dictionary
for enclosure in zoo:
    print("There is a " + zoo[enclosure] + " in " + enclosure)
