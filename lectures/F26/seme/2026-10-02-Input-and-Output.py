# Quiz #4 Today -- While Loops
# Project #2 Assigned Today -- Word Games
# -- see the assignment on web page
#
# Input & Output
# Hey, didn't we already do that?
# Yes --but now for *files*

# Input -- reading from a file

# There are at least 3 ways:


# There are multiple ways to read in a file.  The filename should be a string

# f = open(filename, "r")
# for line in f:
#     data = line.strip()
#
# f.close()

# data will then loop through each line of the file named <filename>

# Or you can read the whole file at once:
# f = open(filename, "r")
# t = f.read()
#
# f.close()

# This reads entire file as a single string

#  *My preferred* way:
#
# with open(filename, 'r') as f:
#     for line in f:
#         data = line.strip()
#         # <do things to data>
#
# f.close()

## Writing to a file
# f = open('temp.txt','w')  # the 'w' means you can write!
# f.write('testing\n')
# f.write('hello\n')
# f.write('bye\n')
# f.close()

# But *be careful*.  If you write to a file, Python will write over *ANYTHING* that is already there!

# When you read in, the incoming information is *always* a string

# When you write, the outgoing info must be a string!