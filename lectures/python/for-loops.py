# For loops
# 29 February (!) 2016
# CSCI 150

# Works, but error-prone.
def explode(s):
    index = 0
    while index < len(s):
        print s[index]
        index += 1

# Better!
def explode_for(s):
    for c in s:    # Do something with every char in the string
        print c
    # shorter, nothing involving indices, less to get wrong.

animals = ['ocelot', 'emu', 'puma', 'koala', 'parrot', 'lion']

def eieio(animals):
    for animal in animals:
        print 'And on this farm he had a ' + animal + '!'

# Input: list of numbers
# Output: sum of the numbers
def oursum(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Input: list of numbers
# Output: a new list with elements twice the input list
#   (input list is unmodified)
def doubled(nums):
    new_nums = []
    for num in nums:
        new_nums.append(num*2)
    return new_nums

# Input: list of numbers
# Output: none
#
# Description: doubles every element in the list.
def double(nums):
    index = 0
    for num in nums:
        nums[index] = 2*num
        index += 1

def double2(nums):
    for index in range(len(nums)):
        nums[index] *= 2

mynums = [1,2,5]

