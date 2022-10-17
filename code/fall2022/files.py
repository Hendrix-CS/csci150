# File I/O  (input/output)

# Reading from a file

# 1. Open the file:

# open takes a file name and a "mode" ("r" = read)
# and returns a "file object".
fin = open("myfile.txt", "r")

# 2. Read from the file.  Two ways:

# .read() puts the entire contents of the file in a string.
# s = fin.read()
#
# print(len(s))
# print(s)

# .readlines() returns a list of strings, one line per string.

# lines = fin.readlines()

for line in fin.readlines():
    l = line.strip()    # chop off space at beginning or end (in this case, \n at end)
    print(len(l))

# 3. Close the file (polite, but not strictly necessary)

fin.close()

# Examples

# codeFile = open("files.py", "r")
# # code = codeFile.read()
#
# for line in codeFile.readlines():
#     line = line.strip()
#     if line != '' and line[0] != '#':
#         print(line)
#
# codeFile.close()

# count: int = 0
# wordFile = open("english3.txt", "r")
# for word in wordFile.readlines():
#     word = word.strip()
#     if not ('q' in word):
#         count += 1
# print(f"The dictionary contains {count} words without e")
# wordFile.close()

# totalLegs: int = 0
# totalStars: int = 0
# count: int = 0
# animalFile = open("animals.txt", "r")
# for line in animalFile.readlines():
#     count += 1
#     data = line.strip().split()
#     name = data[0]
#     legs = int(data[1])
#     stars = int(data[2])
#
#     totalLegs += legs
#     totalStars += stars
#
# print(f"The total number of legs is {totalLegs}.")
# print(f"The average rating is {totalStars / count}")

# Writing to files

# 1. Open the file for writing

fout = open("myfile.txt", "w")

# WARNING!!! This will completely overwrite the file if it exists.

# 2. Write to the file using .write()

fout.write("hello\n")
fout.write("world\n")   # We must add explicit newline characters if we want them!

# 3. Close the file (optional)

fout.close()

# Example: increase all animal star ratings by 1.

from typing import *

# 1. Read information into an appropriate data structure
animals: List[List[str]] = []
animalFile = open("animals.txt", "r")
for line in animalFile.readlines():
    data = line.strip().split()
    animals.append(data)
animalFile.close()

# 2. Process the data
for animal in animals:
    rating = int(animal[2])
    if rating < 5:
        rating += 1

    animal[2] = str(rating)

# 3. Write all the data back out to a file
animalFile = open("animals.txt", "w")
for animal in animals:
    animalFile.write(' '.join(animal) + "\n")
animalFile.close()
