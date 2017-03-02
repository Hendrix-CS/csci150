animals = ['dog', 'frog', 'dolphin', 'spider', 'hog']

# Add three gerbils to the end of animals

# Works!
# while len(animals) < 8:
#    animals.append('gerbil')

# Could also loop until the length is 3 more than it was
# Or loop until a counter reaches 3.

# gerbils = ['gerbil', 'gerbil', 'gerbil']
# Doesn't work (doesn't change animals)
# animals + gerbils
# Works:
# animals = animals + gerbils


# Doesn't work:
# gerbils = 'gerbil'*3
# Works:
# gerbils = ['gerbil']*3
# animals = animals + gerbils

while animals[-3] != 'gerbil':
    animals.append('gerbil')


# Converting between strings and lists of characters (or strings)

# Convert string -> list
# list('hello')
# split()

# Converting list -> string
# join()  -- opposite of split.


nums = [1,2,3]
nums2 = nums
nums.pop()
print(nums2)


# Variables which reference objects that have the same
# value are equal.  You can test this with ==.

# Variables which reference the *same* object are
# "identical".  You can test this with 'is'.

def animal_release(a):
    while len(a) > 2:
        a.pop()




