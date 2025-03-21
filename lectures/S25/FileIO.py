# Reading a (text) file

# 1. "Open" the file

file = open("FileIO.py", "r")    # Open "myfile.txt" for reading ("r")

# 2. Get data out of the file

# 2a. Read all the data at once with .read()

# contents = file.read()
# print(contents)

# OR, 2b. Read all the data as a list of lines with .readlines()

# lines: list[str] = file.readlines()
# count = 0
# for line in lines:
#     if line == "\n":
#         count += 1
# print(f'There were {count} blank lines')
#
# for line in lines:
#     print(line.strip())   # .strip() removes spaces and newline characters from both ends of a string (but not the middle)

# OR, 2c. Read one line at a time with a for loop

# count = 0
# for line in file:
#     if line == "\n":
#         count += 1
# print(f'There were {count} blank lines')

# OR, 2d. Read one line at a time with .readline()

# Print the first and third lines, throw the second line away
# print(file.readline().strip())
# file.readline()
# print(file.readline().strip())

# 3. Close the file (polite)

# file.close()


# Writing to files

# 1. Open the file
# If the file does not exist, it will be created.
# If the file does exist, it will be completely overwritten!!!!!  (Use 'a' to add to the end instead of 'w')
file = open('myfile.txt', 'w')

# 2. Write to the file with .write()

# If we want newline characters, we have to add them ourselves.
# .write() does not add an extra newline like print().
file.write('Hello\n')
file.write('world\n')

# 3. (Polite) close the file.

file.close()