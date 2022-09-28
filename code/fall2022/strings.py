# Strings!

# Strings are sequences of characters.

example = "hello! "
# indices: 0123456

# We can get the character at an individual index using syntax
#    string[index]
# Indices start at 0!
#    e.g.  example[1] == 'e'

# It is an error to access an index that does not exist.

# len(...) gives us the length of a string, i.e. number of characters.

# "" is the empty string, i.e. a string with no characters.

# string[a:b]  is called a "slice"
# it gives us all the characters starting at index a, up to but not including index b.

# We can leave out the first number before the :  --> starts at index 0
# or we can leave out the second number after the : --> continues to the end

# We can concatenate strings with +
# We can duplicate a string with *,
#   e.g.   'hi' * 5 == 'hihihihihi'

# negative indices count from the end of the string: [-1] is the last character, [-2]
#   is second to last, etc.

# strings have "methods" that we can use by writing  string.method()
#   to see them, type help(str).
#
# for example:
#   - x.count(y)   -- counts how many times y appears in x.
#   - x.upper()    -- returns an uppercase version of x
#   - x.lower()    -- same but lowercase.
#   - x.isdigit()  -- we already saw this on a lab, test whether all digits
#   - x.find(y)    -- return the index of the first occurrence of y inside x,
#                     or -1 if it was not found.
#   Other useful ones: strip, split, replace, join, ...

# Let's write our version of count.

# Count how many times the character needle occurs in haystack.
def count(haystack: str, needle: str) -> int:
    n: int = 0   # How many needles have we seen so far?
    i: int = 0   # Current index in the haystack
    while i < len(haystack):
        if haystack[i] == needle:
            n += 1

        i += 1

    return n