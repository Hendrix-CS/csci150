# Monday, 5 October 2015
# Lists, mutability & aliasing, for loops

# Strings are different than lists of characters

# String -> list of characters:
#   list() function
#   string.split(sep)

# list -> string:
#   sep.join(list)

## What will this print??
nums = [1,2,3]
nums2 = nums
del nums[1]
print nums2

def animal_release(zoo):
    while len(zoo) > 2:
        zoo.pop(0)

animals = ['kookaburra', 'lion', 'tiger']
print animals
animal_release(animals)
print animals
