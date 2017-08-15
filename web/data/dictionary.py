import random

# Determines if a word is in the wordfile provided
def valid_word(word, wordfile):
    f = open(wordfile, "r")
    for line in f:
        if line.lower().strip() == word.lower():
            return True
    return False

# Finds a random word in the wordfile
def random_valid_word(wordfile):
    f = open(wordfile, "r")
    t = f.readlines()
    r = int(random.random() * len(t))
    return t[r].strip()
