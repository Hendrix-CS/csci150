import random

# Determines if a word is in the wordfile provided
def valid_word(word: str, wordfile: str) -> bool:
    f = open(wordfile, "r")
    for line in f:
        if line.lower().strip() == word.lower():
            return True
    return False

# Finds a random word in the wordfile
def random_valid_word(wordfile: str) -> str:
    f = open(wordfile, "r")
    t = f.readlines()
    r = int(random.random() * len(t))
    return t[r].strip()
