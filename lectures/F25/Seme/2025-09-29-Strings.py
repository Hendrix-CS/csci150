# Reminders:
#  Project #1 Due Wednesday

# Quiz #4 Friday -- While Loops



# STRINGS!

# We have used strings a bit previously. A string is just an ordered list of characters

# Today we will learn how to work with and manipulate them

# I am going to not use functions today, since we are really just learning syntax.
# Instead, I am going to comment code in and out

s = 'My string'
t = 'abcdefg'

# Concatenation:


# print(s + t)
# print(t + s)
#
# print(s * 3)


# We can access the individual characters of a string by their index.
# The first character has index 0. This is weird at first, but you get used to it.

# print(s[3])
# print(s[0])
# print(s[5])
# print(t[3])


# We can also get a 'slice' of a string:

# print(s[1:6])
# print(s[1:2])
# print(s[1:3])

# The syntax is str[a:b] will return from index a to index b - 1.
# This is also weird, but again, you get used to it

# print(s[4:])  #starts at index 4, goes to end
#
# print(s[:4])  # starts at index goes, goes up to, does not include 4
#
# print(s[:4] + s[4:])

#print(s[:])  # starts at 0, goes to end (i.e. the whole string)

#print(s[4:4]) # prints ''

# The empty string ''



#print(s[-4]) # -4 is the 4th character from the end

#print(s[-1]) # prints the last character


#print(s[-4:-1])

#print(s[-9])



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

# print( s[:5] + s[6 : ]     )


# String Methods & Functions
# There are a number of built-in Python functions that act on strings
# Formally, most of these are called 'methods,' as they act on members
# of a data class (the 'str' class) and the members are formally called 'objects.'
#
# We'll return to this nomenclature later in the semester
# For now, you can think of them as built-in functions

# # Length -- a function, which returns the number of characters in a string
# print(len(s))
# print(len('aaa'))
# # #
# print(len(''))
#
# print(s[0: len(s)])
#
# print(len(s) == len(t))


# Other examples (these are all methods)

# upper:
# print(s.lower())
# print(s)

# s = s.upper()
# #print(s.upper())
# print(s)
#
# # lower
#print(s.lower())
#
# print(s) #notice that s.lower() and s.upper() don't actually change s
#
# print('fbXtR%& *'.lower())

# count

# print(s.count('x'))
# print(s.count('n'))
# #
# print('abcABCabcdeab'.count('abc'))

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

# If time allows, we'll consider these two examples below:

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