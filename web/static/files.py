# File I/O (Input/Output)

# Think of a text file as a big string.

# 1. Writing to a file:

# Opens the file for writing (creates it if doesn't exist)
# and assigns a 'file object' to fout.
fout = open("myfile.txt", "w")

# Write strings to the file using the write function.  Unlike
# print(...), you have to add newline characters yourself.
fout.write("hello")
fout.write("world\n")

# Close the file when done.
fout.close()


# 2. Reading from a file:

# Opens a file in reading mode
fin = open("files.py", "r")

# Option 1: use a for loop to get the file line by line.

fin = open("files.py", "r")
for line in fin:

    # Just an example.
    if (line != '' and line[0] == '#'):
        print(line.strip())
        # The strip() is important: it removes the newline character
        # at the end of the line.

# Close the file when done.
fin.close()


# Option 2: Get the entire contents of the file as a single string.

fin = open("files.py", "r")
s = fin.read()
print(s)
print(len(s))

lines = s.split("\n")
print(len(lines))

fin.close()


