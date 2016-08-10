# CSCI 150
# 19 Feb 2016
# Strings!

# Strings are sequences of characters.
# We can ask for a character at a particular position or *index*
#   using  string[i] notation.
# Indices start at 0!

# Length of a string: len().

# Indices too big give a runtime error
# Negative indices count backwards from end.

# Slices:
#   mystring[a:b]  -- starts at index a, up to but NOT INCLUDING index b.
#   negative indices work too
#   can omit one or both indices -- start @ beginning or go to end.

# Operations on strings:
#   We've seen + (concatenation)
#   * does repetition  (e.g.  mystring * 3)
#   Methods:
#      call like string.method()
#      - upper()
#      - count(sub)
#      - replace(old, new)
#      - isdigit()
#      - find(sub)

#### String + loop practice

def explode(s):    # print every character of s on a line by itself.
    index = 0
    while index < len(s):
        print s[index]
        index = index + 1

def explode2(s):
    while (len(s) > 0):
        print s[0]
        s = s[1:]
