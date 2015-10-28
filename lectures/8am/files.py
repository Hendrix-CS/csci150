# File input & output  (File I/O)
#
# Reading from a file:

f = open("test.txt", "r")
  # open test.txt, in "read mode"

# Read everything into one giant string:

file_contents = f.read()

# Once you are done:

f.close()

f = open("test.txt", "r")

for line in f.readlines():
    print len(line.strip())

f.close()

# Writing to files

f2 = open("output.txt", "w")

f2.write("This is a string.\n")
f2.write("This is another one.\n")

f2.close()

in_file = open("test.txt", "r")
out_file = open("test_rev.txt", "w")

for line in in_file.readlines():
    chars = line.strip().split()
    chars.reverse()
    out_file.write("".join(chars) + "\n")

in_file.close()
out_file.close()
