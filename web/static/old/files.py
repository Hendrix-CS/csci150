# File I/O (Input/Output)

# Think of a text file as a big string.

# 1. Writing to a file:

# Opens the file for writing (creates it if doesn't exist)
# and assigns a 'file object' to fout.
fout = open("myfile.txt", "w")

fout.write("hello")
fout.write("world\n")
fout.close()


# 2. Reading from a file:

# Opens a file in reading mode
fin = open("files.py", "r")

# Option 1: entire contents as a single string.
s = fin.read()
print(s)
print(len(s))

lines = s.split("\n")
print(len(lines))
print(lines[8])

# Note t is empty string, since the file has already been read
t = fin.read()
print(t)

fin.close()

fin = open("files.py", "r")

t = fin.read()
print(len(t))

fin.close()

# Option 2: readlines()

fin = open("files.py", "r")
for line in fin:
    if (line != '' and line[0] == '#'):
        print(line.strip())
fin.close()

