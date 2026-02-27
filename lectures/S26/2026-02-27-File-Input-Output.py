import random
import spellcheck

# Quiz #4 Today -- While Loops
# Homework #5 Strings, due Monday
#
# I have completed assessing all projects which have been turned in.
# Please check if you warned all points and make sure you understand
#    what to do if you did not.

# Project #2 is assigned today

# Let over from Wednesday:

# Finally, write in_order(s), which takes in a string and returns
# True when the letters are in alphabetical order -- counting repeats as being ok

# 'loop' would return True
# 'while' would return False

def in_order(s: str) -> bool:
    i = 0

    while i < len(s) - 1:
        # if not in order return False
        if s[i] > s[i + 1]:
            return False


        i += 1

    return True

    # only return True if we make it to the end







## Reading from and writing to a file

# Reading from a file

# There are multiple ways to read in a file.  From the 'spellcheck.py' module:

# f = open(wordfile, "r")
# for line in f:
#     data = line.strip()
#
# f.close()

# data will then loop through each line of the file named <wordfile>

# Or you cna read the whole file at once:
# f = open(wordfile, "r")
# t = f.readlines()
#
# f.close()

# t would be a list of word -- we'll talk about lists formally next week

# Writing to a file
f = open('temp.txt','w')  # the 'w' means you can write!
f.write('testing\n')
f.write('hello\n')
f.write('bye\n')
f.close()

# But *be careful*.  If you write to a file, Python will write over *ANYTHING* that is already there!

# When you read in, the incoming information is *always* a string

# When you write, the outgoing info must be a string!