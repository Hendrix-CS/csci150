# Reading + writing files!

# How to read from a file.

# 1. Open the file.

file = open('files2.py', 'r')

# 2. Read data from the file, using:
#   - file.read()   (read the entire contents of the file as a string)
#   OR
#   - file.readlines()   (returns a list of strings, each one is one line of the file)

# 3. Close the file (polite):   file.close()


# How to write to a file.

# 1. Open the file:    file = open(filename, 'w')    (creates a new file if it does not exist; overwrites it if it does)

# 2. Write to the file with   file.write(str)

# 3. Close the file.