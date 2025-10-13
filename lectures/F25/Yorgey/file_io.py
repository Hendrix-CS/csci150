import random

## 1. Reading from a file.

file = open('test_file.txt', 'r')   # Name of file to open, mode ('r' = read)
  # file is a "file object"

## 1a. Read the entire file at once.

contents = file.read()

print(f'The file contains {len(contents)} characters.')
print('Here it is:')
print(contents)

words = contents.split()
print(f'Here is a random word from the {len(words)} words in the file: {random.choice(words)}')

# Close the file when finished.  Not strictly necessary, but polite.
file.close()

## 1b. Read the file one line at a time.

dict_file = open('english3.txt', 'r')

# Read the file into a list of strings, one string per line.
wordlist = dict_file.readlines()

print(f'There are {len(wordlist)} lines in the file')

print(wordlist[5])
i = 0
search_word = ''
while i < len(wordlist):
    word = wordlist[i].strip()
    if word == search_word:
        print(f'Found {search_word} at index {i}')
    i += 1

e_count = 0
i = 0
while i < len(wordlist):
    # Count # of words with at least one e
    # if 'e' in wordlist[i].strip():
    #     e_count += 1

    e_count += wordlist[i].count('e')

    i += 1

print(f'There are {e_count} words that contain the letter e.')

dict_file.close()


# 2. Writing to a file

# CAUTION!!!  Opening a file for writing will create it, or instantly erase it.
file = open('output.txt', 'w')

# We can use file.write()  to output stuff to the file.

file.write('Hello\n')
file.write('world\n')

file.close()