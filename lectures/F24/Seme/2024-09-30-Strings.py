# Reminders:
#  -- New Homework -- Function Stack Tracing, due next Monday
#  -- Quiz Wednesday -- Conditionals
#  -- Project #1 due  Friday, 9/4

# STRINGS!

# We have used strings a bit previously. A string is just an ordered list of characters

# Today we will learn how to work with and manipulate them

s = 'My string'
t = 'abcdefg'

# Concatenation:


#print(s + t)

#print(s * 3)


# We can access the individual characters of a string by their index.
# The first character has index 0. This is weird at first, but you get used to it.

# print(s[3])
# print(s[0])
# print(s[5])
# print(t[3])

# slice
#print(t[1:4])

# We can also get a 'slice' of a string:

#print(s[1:6])

# The syntax is str[a:b] will return from index a to index b - 1.
# This is also weird, but again, you get used to it

#print(s[4:])  #starts at index 4, goes to end

#print(s[:4])  # starts at index goes, goes up to, does not include 4

#print(s[:])  # starts at 0, goes to end (i.e. the whole string)

# print(s[4:4]) # prints ''
# print('Hello' == 'Hello ')
# print('Hello ')
# print(5)
# print('5')


#print(s[-4]) # -4 is the 4th character from the end

#print(s[-1]) # prints the last character


#print(s[-4:-1])

# print(s[-1:-4])
# print(s[5:2])

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

# Length -- a function, which returns the number of characters in a string
# print(len(s))
# print(len('aaa'))
# #
# print(len(''))
#
# print(len(s) == len(t))

# The special string '' is the null string

# Other examples (these are all methods)

# upper:

# s = s.upper()
# #print(s.upper())
# print(s)
#
# # lower
#print(s.lower())
#
# print(s) #notice that s.lower() and s.upper() don't actually change s
#
#print('fbXtR%& *'.lower())

# count

#print(s.count('x'))
#
#print('abcABCabcdeab'.count('b'))

#print('abcABCabcdeab'.count('a'))

# find

#print(s.find('t'))
#
#print('abcdabcdabcde'.find('z'))

# replace

# print(s.replace('y','TTT'))
# #
# print('abcdabcdabcd'.replace('b',"X"))


#print('12303'.isdigit())

#print('-12303'.isdigit())


def string_counter(s: str, char: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] == char:
            count += 1
        i += 1
    return count


def string_replace(s: str, old: str, new: str) -> str:
    new_str = ''
    i = 0
    while i < len(s):
        if s[i] == old:
            new_str += new
        else:
            new_str += s[i]

        

        i += 1

    return new_str