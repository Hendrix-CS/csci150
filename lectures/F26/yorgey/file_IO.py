# Reading + writing text files

# Text files are really just giant strings!

# 1. How to read from a file
#
# 1a. Read the file as one giant string

# open strings.py in "read mode".  'file' is a variable
# that will keep track of the file for us.
# file = open('strings.py', 'r')
#
# contents = file.read()   # read the entire file as one big string, assign it to 'contents'
#
# print(contents)
# print(f'The file contains {len(contents)} characters.')
#
# file.close()   # Polite to close the file when finished reading it

# 1b. Read the file line by line.
#
# file = open('strings.py', 'r')
#
# for line in file.readlines():   # Loop through each line of the file one by one.
#     line = line.strip()   # Get rid of special newline character at the end of line
#     if line != '':
#         print(line)    # Print only the non-blank lines.
#
# file.close()

# 2. Writing to a file

file = open('myfile.txt', 'w')   # Create or OVERWRITE (!!!) the file!

file.write('hello!\n')
file.write('CSCI 150\n')

file.close()