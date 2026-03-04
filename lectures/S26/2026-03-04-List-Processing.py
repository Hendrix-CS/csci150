import spellcheck

# Reminders
# Quiz #5 (Strings) this Friday
#
# New Homework #6 (Lists) Assigned today -- due Monday
#
# Project #2 due in about 2 weeks

# Last time, we saw that lists are a lot like strings:
# * Ordered collection of items
# * Have indices
# * Have length
# * Can access individual items or slices

# The basics of processing a list *also* works a lot like strings:
#
#

# Given a list of integers, return the sum:
# lst = [5, 2, 9, 1]
def list_sum(lst: list[int]) -> int:
    i = 0
    sum = 0
    while i < len(lst):
        sum += lst[i]

        i += 1

    return sum


# even_sum -- given a list of integers, return the sum,
# but only of the *even* numbers in the list
def even_sum(lst: list[int]) -> int:
    i = 0
    sum = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            sum += lst[i]

        i += 1

    return sum



# Given a list of strings, return True only if every word is at least 6 letters long
def long_words(lst: list[str]) -> bool:
    i = 0

    while i < len(lst):
        if len(lst[i]) < 6:
            return False

        i += 1

    return True

# valid_words
# Given a list of strings, return True only if all are valid, using:
# * the spellcheck.py module &
# * the english3.txt dictionary
# from the Doublets lab
#
# You will need to make sure that both above files are in the same
# folder as this file

def valid_words(lst: list[str]) -> bool:
    i = 0

    while i < len(lst):
        if not spellcheck.valid_word(lst[i], 'english3.txt'):
            return False

        i += 1

    return True



# Given a list of integers, triple any value that is even
def triple_evens(lst: list[int]):
    i = 0

    while i < len(lst):
        if lst[i] % 2 == 0:
            lst[i] *= 3
        i += 1


# Given a list of integers, return a *new* list
# which triples any value that is even
def triple_evens_new(lst: list[int]) -> list[int]:
    i = 0
    mst = []
    while i < len(lst):
        if lst[i] % 2 == 0:
            mst.append(lst[i] * 3)
        else:
            mst.append(lst[i])
        i += 1

    return mst
    