# First, we'll look at a tracing example with while loops (the solutions is shown at the end of the
# tracing examples from last week)

# One thing to notice: It is vitally important that the incremental variable
#   inside the while loop gets updated!

def while_ex(n: int) -> int:
    i = 0
    j = 0
    while i < n:
        j += i
        i += 1

    return j

def main4():
    print(while_ex(3))
    print(while_ex(4))

#main4()


# And now strings:

# We have used strings a bit previously. A string is just an ordered list of characters

# Today we will learn how to work with and manipulate them

s = 'My string'
t = 'abcdefg'

# Concatenation:


#print(s + t)

#print(s * 3)


# We can access the individual characters of a string by their index.
# The first character has index 0. This is weird at first, but you get used to it.

#print(s[-1])
#print(t[3])

# slice
#print(t[1:4])

# We can also get a 'slice' of a string:

#print(s[1:6])

# The syntax is str[a:b] will return from index a to index b - 1.
# This is also weird, but again, you get used to it

#print(s[4:])

#print(s[:4])

#print(s[:])

#print(s[4:4])

#print(s[:])

# the slice s[:] does the whole string -- and is never really useful!


#print(s[-4])
# -4 is the 4th character from the end

#print(s[-1])
# prints the last character

#print(s[-4:-1])

#print(s[-1:-4])

#Index Errors
#print(s[12])

#print(s[-20])

# Slices never produce index errors:
#print(s[100:103])
#print(s)
#print(s[2:-3])

#print(s[-3:8])

#Even poorly formed slices:
#print(s[5:2])


# String Methods & Functions
# There are a number of built-in Python functions that act on strings
# Formally, most of these are called 'methods,' as they act on members
# of a data class (the 'str' class) and the members are formally called 'objects.'
#
# We'll return to this nomenclature later in the semester
# For now, you can think of them as built-in functions

# print(len(s))
# print(len('aaa'))
#
# print(len(''))

# The special string '' is the null string

# Other examples (these are all methods)

# upper:

# print(s.upper())
#
# # lower
# print(s.lower())
#
# print(s)
#
# print('fbXtR%& *'.lower())

# count

# print(s.count('y'))
#
# print('abcABCabcdeab'.count('b'))

#print('abcABCabcdeab'.count('a'))

# find

# print(s.find('t'))
#
# print('abcdabcdabcde'.find('z'))

# replace

print(s.replace('y','TTT'))

print('abcdabcdabcd'.replace('b',"X"))

# is_digit()

#print(s.isdigit())

#print('12303'.isdigit())

#print('-12303'.isdigit())

## We got to here today ##

def string_counter(s: str, t: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] < t:
            count += 1
        i += 1
    return count