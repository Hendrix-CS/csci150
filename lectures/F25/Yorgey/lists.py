# Python *lists* allow us to store a sequence of arbitrary values,
# similar to how strings store a sequence of characters.

# To make a list, use square brackets with items separated by commas.
my_nums: list[int] = [1, 2, 3]
  # list[int] means it is a list of ints, i.e. a list whose items are all int.

animals: list[str] = ['burro', 'kangaroo', 'wallaby', 'sloth']

list_of_lists: list[list[bool]] = [[True, False], [True, True, True], [False, False], []]

empty_list = []

# Python allows us to have lists containing different types,
# but we will never do this.
allowed_but_terrible = [2, 'hello', 3.1415, [6, False]]


## Ways that lists are similar to strings!

# We can get the item at a particular index:
print(animals[1])      # 'kangaroo'

# We can ask for the length:
print(len(animals))    # 4

# We can get slices:
print(animals[1:3])

# We can put lists together ("concatenate") with +:
print(['horse'] + animals + ['whale', 'polar bear'])

# error: can't add list + string
#  print(animals + 'horse')

# Can replicate a list with *:
print(animals * 3)


## Strings are *immutable*, lists are *mutable*.

# e.g.
#   word = 'dangeroo'
#   word[0] = 'k'  is an error

# but
animals[1] = 'tiger'   # works, changes 'kangaroo' to 'tiger'
print(animals)

animals.append('panda')   # modifies the list by adding a new item on the end.
print(animals)

animals = animals + ['giraffe']   # also works, but slow
print(animals)

# Take a list of ints as input, add them all up and return their sum.
def sum_list(nums: list[int]) -> int:
    index: int = 0
    sum: int = 0
    while index < len(nums):
        sum += nums[index]
        index += 1
    return sum
