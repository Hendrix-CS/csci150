# Reminders:
#
# Project #2 due Wednesday!

# Office Hours
# Monday: 10:30  - 3 pm
# Tuesday: 1ish - 3pm

#
# For loops quiz on Friday




# In the Caesar's Secrets Lab you had to write a function to find
# the letter frequency. This was somewhat difficult, since you
# had to continually remember how to match the index and the location
# in a list -- is the 't' index 20 or 21 or 19 or ...

# What if there was a better way!?!?!?

# Today, we will learn about a new data type in Python,
# a dictionary!!!!

# Think about a simple, real-world dictionary
# Each entry contains:
#   -- a key   -- that is the word you look up
#   -- a value -- information associated with that key (the definitions, etymology, etc)

# That is essentially how a Python dictionary works:

# Each entry is a pair of key
#    (which can only be immutable: strings, integers, floats, tuples for us)
# and a value, which can be anything -- string, int, lists, even another dictionary

# One major advantage of a dictionary is that finding the key is easy

# Simple contrived example:

# First, look at a list, which lists the current enrollments
# in each of the 100-level CSCI classes:
# CSCI 150 01 (this class)
# CSCI 150 02 (Dr. Yorgey's lecture)
# CSCI 150 L1 (Dr. Yorgey's Lab)
# CSCI 150 L2 (Dr. Develan's Lab)
# CSCI 151 01
# CSCI 151 L1

#lst = [26, 16, 19, 23, 9, 9]

# is essentially the matching
# 0 -> 26
# 1 -> 16
# 2 -> 19
# 3 -> 23
# 4 -> 9
# 5 -> 9


# The indices 0, 1, 2, ... are the *keys*, while the
# enrollments are the *values*  Each key maps to a single value.
#
#  A dictionary is just an extension of this, except that instead of requiring
#  the keys to be consecutive integers starting at 0,
#  we can have *arbitrary* keys!
#
#
# Suppose that we did this:
# 'CSCI15001' -> 26
# 'CSCI15002' -> 16
# 'CSCI150L1' -> 19
# 'CSCI150L2' -> 23
# 'CSCI15101' -> 9
# 'CSCI151L1' -> 9

# In the list version, we have to remember which index corresponds to
# which class -- that's difficult!

# It is much easier if the key has some *meaning* to the human programmer.

#  One important point:  The keys themselves must be immutable --
#  that is they can only be ints, str, floats, booleans
#   you cannot use a list or a dictionary as the key in a dictionary.

#  Okay, so now what:
#  The following is a dictionary for our classes:

# csci_dict: dict[str,int] = {'CSCI15001': 26, 'CSCI15002': 16, 'CSCI150L1': 19,
#                             'CSCI150L2': 23, 'CSCI15101': 9, 'CSCI151L1': 9}
#
# # Notice the syntax -- we use { curly braces } to tell Python
# # # what follows is a dictionary
# # # we separate the key and the value with a colon :
# print(csci_dict['CSCI15001'])
# print(csci_dict['CSCI150L2'])
# csci_dict['CSCI150L2'] += 1
#
# print(csci_dict['CSCI150L2'])
#
# # # Run this in the console and type:      csci_dict['CSCI151L1']
# #
# # #print(csci_dict['CSCI12301'])
# #
# # # You got an error, since the dictionary does not have a value for that key
# # # -- this is like asking for
# # #    s[6] when s = 'abc'.
# #
# # ##############
# # # Modifying dictionaries
# # ##############
# #
# # # You can directly modify the value for a key:
# # csci_dict['CSCI15001'] = 24
# # print(csci_dict)
# #
# # # You can add a new key/value pair:
# # csci_dict['CSCI12301'] = 123
# # print(csci_dict)
# # # # You can delete a key / value pair by:
# # del csci_dict['CSCI15001']
# # print(csci_dict)
# # #
# # # print(csci_dict)
# # #

csci_dict: dict[str,int] = {'CSCI15001': 26, 'CSCI15002': 16, 'CSCI150L1': 19,
                            'CSCI150L2': 23, 'CSCI15101': 9, 'CSCI151L1': 9}
# # Iterate over all keys using for
#
for k in csci_dict:
    print(f'{k} has {csci_dict[k]} students enrolled.')
#
# print(csci_dict)
#
# # The number of keys in a dictionary is given by len(dictionary_name)
print(len(csci_dict))
# #
print(list(csci_dict.keys() )) #will return a list of all keys in the dictionary
# #
print(csci_dict.keys())
# #
# #dictionary_name.values()  will return a list of all values (including any duplicates!)
print(list(csci_dict.values()))
#
# # to see if a key is in a dictionary, use in:
# print('MATH13001' in csci_dict)
# print('CSCI15001' in csci_dict)
# print(12 in csci_dict)
#
# print(12 in list(csci_dict.values()))
#
# ######## Important info with dictionaries
# # Each key maps to a single value (which can be any one thing
# # -- a str, an int, a float, or even a list
# #   or another dictionary!
# # It is possible that multiple keys might have the same value, though
#
# # You can easily look up by key.  You cannot look up by value
# #  That is, given a key, we can ask the dictionary for its matching value.
# #  Given a value, we cannot directly ask the dictionary which key(s) it is associated with
#
# # This is like a regular language dictionary:
# #  It is easy to look up what a word means
# #  It is difficult to use a dictionary to find a word which has a
# #   specific given meaning
#
#
# # Now, let's try to do the letter_freq count
# #
def list_freq_count(s: str) -> list[float]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = [0] * 26
    for char in s.lower():
         if char in alphabet:
             ind = alphabet.index(char)
             freq_list[ind] += 1

    i = 0
    total = sum(freq_list)

    for entry in freq_list:
        freq_list[i] = freq_list[i] / total
        i += 1
    return freq_list
# #
# #
# #
#
def dict_freq_count(s: str) -> dict[str, float]:
    freq_dict = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        freq_dict[char] = 0
    total = 0
    for char in s.lower():
        if char in alphabet:

            freq_dict[char] += 1
            total += 1

    for key in freq_dict:
        freq_dict[key] /= total

    return freq_dict
# #
#
word_file = open('alice.txt','r')
s = word_file.read()
word_file.close()

freq_list = list_freq_count(s)
print(freq_list)

freq_dict = dict_freq_count(s)
print(freq_dict)
#
#
#

