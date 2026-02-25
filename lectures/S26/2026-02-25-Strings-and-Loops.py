# Project #1 Due now

# New Homework -- Strings:
# * Some "by hand"
# * Some CodingBat
# Due on Monday

# Quiz #4 on Friday -- While Loops

# Last time, we saw the basic of strings:
# * Indices
# * Slices
# * Length
# * Basic Methods: .find(), .count(), .upper(), .lower(), etc

# Today, we will learn how to "process" a string
# - that is, go character by character through a string and do things

# "Explode" a string -- given a string, print each character, one at a time

def explode_str(s: str):
    i = 0

    while i < len(s):
        print(s[i])
        i += 1



# The basic syntax:
#
# i = 0
# <maybe other variables>
# while i < len(s):
#   <do stuff>
#
#   i += 1

# This lets us "walk" across the string one character at a time

# Let's replicate the built in .count() method:


def count_char(s: str, c: str) -> int:
    i = 0
    counter = 0
    while i < len(s):
        if s[i] == c:
            counter += 1
        i += 1
    return counter











def find_char(s:str, c: str) -> int:
    i = 0

    while i < len(s):
        if s[i] == c:
            return i

        i += 1

    return -1




# Insert character:
# Given a string s, a character c, and index i, we want to insert
# c at position i into s:

# Example:  insert_char("testing", "q", 3)
# would return "tesqting"


def insert_char(s: str, c: str, i: int) -> str:
    j = 0
    return_str = ''
    while j < len(s):
        if i == j:
            return_str += c
        return_str +=s[j]

        j += 1

    return return_str


# **** We did not get to this one in class; We will do it first on Friday.

# Finally, write in_order(s), which takes in a string and returns
# True when the letters are in alphabetical order -- counting repeats as being ok

# 'loop' would return True
# 'while' would return False

def in_order(s: str) -> bool:
    1




