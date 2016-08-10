# CSCI 150
# Wednesday, 7 October
# For loops

# 1. Copying a list
# 2. Functions that mutate vs. making a new object

# For loops!

def explode(s):
    index = 0
    while index < len(s):
        print s[index]
        index += 1
# Lots of things can go wrong in the above code:
#   - wrong starting index
#   - wrong test
#   - forget to increment

# Better:
# None of the above can go wrong!

def explode_for(s):
    for c in s:
        print c

# Above is with a string
# Also works with lists

def double(nums):
    """Takes a list of numbers and doubles
    all the numbers."""
    index = 0
    while index < len(nums):
        nums[index] = nums[index] * 2
        # or nums[index] *= 2
        index += 1

# Can we do the above with a for loop?

#def double_for(nums):
 #   for n in nums:
        # n = 2 * n   # doesn't work...?
           # only modifies n, not the original list
        # nums[n] *=2    # doesn't work either

        # seems like we really need the list
        # indices to do this!  For loop doesn't
        # give us indices.

def double_for2(nums):
    for index in range(len(nums)):
        nums[index] = nums[index] * 2

def double_string(s):
    new_str = ""
    for ch in s:
        new_str = new_str + ch * 2
    return new_str

##### For loop practice

def count(s, c):
    """Count how many times the character c
    appears in the string s."""
    count = 0
    for index in range(len(s)):  # or: for c2 in s 
        if s[index] == c:            # or:    if c2 == c:
            count +=1
    return count

def find(s,c):
    """Find the index of the first occurrence of c in s,
    or return -1 if s does not contain c."""
    



    
