# Making dictionaries

# Dictionaries are written
#   { key1: value1, key2: value2, key3: value3, ... }

zoo = {'A23': 'tapir', 'B9': 'ferret', 'Z12': 'alligator'}

# We can look up or modify the value associated with a particular key
# using indexing notation, just like with lists.  e.g.

print(zoo['B9'])
zoo['Z12'] = 'elephant'
print(zoo)

# Trying to access the value associated to a key that doesn't exist
# is an error.
# print(zoo['Q72'])

# Traceback (most recent call last):
#   File "/home/brent/PycharmProjects/Dictionaries/dictionaries.py", line 15, in <module>
#     print(zoo['Q72'])
# KeyError: 'Q72'

zoo['Q72'] = 'komodo'
print(zoo)

# Alternative way to create zoo dictionary: start w/ empty dictionary and add
# items one by one.
zoo2 = {}   # empty dictionary
zoo2['A23'] = 'tapir'
zoo2['B9'] = 'ferret'
zoo2['Z12'] = 'elephant'
zoo2['Q72'] = 'komodo'

print(zoo == zoo2)

# Some other things we can do w/ dictionaries:

# Get a list of all the keys with .keys()

for k in zoo.keys():
    print(k)

# Get a list of all the values with .values()

for animal in zoo.values():
    print(animal)

# Can actually iterate through all the keys in a for loop without writing .keys():

for k in zoo:
    print(f'Enclosure {k} holds a {zoo[k]}.')

# Get the size (i.e. number of key/value pairs) with len

print(len(zoo))

# Delete a key/value pair with del:

del zoo['Z12']
print(zoo)