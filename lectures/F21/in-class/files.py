# Files!

# 1. Write to a file.

# Open a file for writing ("w")
#   Create it if it does not exist
#   Replace the contents if it does exist
out_file = open("myfile.txt", "w")

# To write data to the file, use .write(str):
out_file.write("Hello\n")
out_file.write("world\n")

for i in range(10):
    out_file.write(f'{i}\n')

# Polite to close when we are done.
out_file.close()

# 2. Reading from a file

in_file = open("files.py", "r")

# Two ways to get the contents of the file.
# a) Get the entire contents of the file
#    as one giant string using .read()

# contents: str = in_file.read()

# b) Read the file line by line using
#    .readlines() - gives us a list
#    of strings, one per line.
#    Note, each line contains a newline character
#    at the end.  To get rid of them, we can use
#    .strip() .

for line in in_file.readlines():
    # print(len(line.strip()))
    if 'c' in line:
        print(line.strip())

in_file.close()