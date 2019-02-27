from typing import *

# Print the items in the list, one per line
def explode_list(items: List[str]):
    i: int = 0
    while i < len(items):
        print(items[i])
        i += 1


# Strings and lists
# String is a sequence of characters, a list is a sequence of anything you like
# They are quite similar, but not the same.

# To convert a string to a list:
# 1. Use the list() function
#    e.g.  list("hello")
# 2. Use the split() function on a string.
#    e.g. "banana".split("n")
#    or e.g.  "this is a sentence".split()  # splits on spaces by default.

# To convert a list of strings into a string:
# - Use the join function.

# " -> ".join(['fun', 'sun', 'sub', 'bub'])
# 'fun -> sun -> sub -> bub'
# "\n".join(["This is a line", "This is another line", "Third line"])
# 'This is a line\nThis is another line\nThird line'
# print("\n".join(["This is a line", "This is another line", "Third line"]))
# This is a line
# This is another line
# Third line



# Goal: add three gerbils to the end
animals: List[str] = ["parakeet", "iguana", "octopus", "wombat"]

# gerbils: List[str] = ['gerbil', 'gerbil', 'gerbil']

# Doesn't work (doesn't change animals)
# animals + gerbils

# WORKS
# animals = animals + gerbils

# WORKS
# animals = animals + ['gerbil', 'gerbil', 'gerbil']

# WORKS
# animals = animals + ['gerbil'] * 3

# Doesn't work (gives a string with gerbils in)
# animals = ' gerbil '.join(animals)

# Sort of works?  All the gerbils are in one string
# animals.append('gerbil' * 3)

# All the gerbils are still in one string
# animals.append('gerbil ' * 3)

# Doesn't work: append adds *one thing* to the end of a list,
# so we get a list whose last member is a list of three 'gerbil's
# animals.append(['gerbil'] * 3)