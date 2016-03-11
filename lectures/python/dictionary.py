#######################################################################
# Program:   Dictionary
# Author:    Mark Goadrich
# Date:      4/2/2000 for Java 4/17/2007 for Python
#######################################################################

def valid_word(word, file):
    """ Finding if a word is valid in the English dictionary """
    # We need a Dictionary to tell us if we have valid words
    webster = open(file, 'r')

    # Loop through the words until you find what you're looking for
    # Could be faster with binary search (extra credit?)
    for line in webster:
       if word.lower() == line.lower().strip():
           return True

    # Word was not found, so it is invalid
    return False
