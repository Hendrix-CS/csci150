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


# Finds the max value in a list
def xyz(m):
    p = m[0]
    for g in m:
        if g > p:
            p = g
    return p

# print xyz([3,6,2,9,3,0])

# Returns true iff there is a repeated element [...,x,x,...]
def abc(q):
    for y in range(len(q) - 1):
        if q[y] == q[y+1]:
            return True
    return False

# print abc([1,3,5,3,5])
# print abc([1,1])

# Input: list of numbers
# Output: boolean, True if nums is sorted from smallest
#   to biggest
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False
    return True

##print is_sorted([1,3,5,6,8,10])
##print is_sorted([1,5,2,6,3,7,4])
##print is_sorted([1,2,3,3,4,5])

# Input: string s, character c
# Output: first index of c in s, if it exists,
#    or -1 if c is not in s.
#
# e.g.  find_char("banana", 'n') == 2
#          find_char("banana", 'x') == -1
def find_char(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1

print find_char("banana", 'n')
print find_char("banana", 'x')

# Input: string s, character c
# Output: list of all indices in s that are equal to c
#   (if c is not in s, return the empty list)
def find_all_chars(s, c):
    indices = []
    for i in range(len(s)):
        if s[i] == c:
            indices.append(i)
    return indices
    
print find_all_chars("banana", 'n')
print find_all_chars("banana", 'x')

# Input: a list of floats
# Output: their average
def average(floats):
    total = 0
    for f in floats:
        total += f
    return total / len(floats)





