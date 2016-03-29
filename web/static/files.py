# 28 March 2016
# File I/O

# 1. Create a file object using 'open' function.

input_file = open ("test.txt", "r")
  # "r" means "read mode"

# 2. Get content from the file

file_contents = input_file.read()
  # Get entire contents as single string

# 3. Close file

input_file.close()   # polite


input_file = open("test.txt", "r")

word_count = 0
for line in input_file.readlines():
    word_count += len(line.split())

print "The file has " + str(word_count) + " words."

input_file.close()   # polite

###### Count words ###########3LOL!!11

input_file = open("test.txt", "r")

word_counts = {}
for line in input_file.readlines():
    line = line.lower()
    for word in line.split():
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

for word in word_counts:
    print word+ " occurs " + str(word_counts[word]) + " times."

## Writing to a file ##########

# 1. Open in write mode.
output_file = open("output.txt", "w")

output_file.write("Some text.\n")

output_file.close()



