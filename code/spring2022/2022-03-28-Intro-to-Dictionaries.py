from typing import *

# Reminders:
#
# Project #2 is assigned -- it is due in two weeks
# CodingBat Homework is due this coming Friday
# Exam #2 Redos are due on Monday of next week



# In the Caesar's Secrets Lab you had to write a function to find
# the letter frequency. This was somewhat difficult, since you
# had to continually remember how to match the index and the location
# in a list

# What if there was a better way!?!?!?

# Today, we will learn about a new data type in Python,
# a dictionary!!!!

# Think about a simple, real-world dictionary
# Each entry contains:
#   -- a key   -- that is the word you look up
#   -- a value -- information associated with that key (the definitions, etymology, etc)

# That is essentially how a Python dictionary works:

# Each entry is a pair of key (which can only be immutable: strings, integers, floats, tuples for us)
# and a value, which can be anything -- string, int, lists, even another dictionary

# One major advantage of a dictionary is that finding the key is easy

# Simple contrived example:

# First, look at a list

#lst = ['dog', 'cat', 'horse']

# is essentially the assignment
# 0 -> 'dog'
# 1 -> 'cat'
# 2 -> 'horse'

# The indices 0, 1, 2 are the *keys*, while the animal names are the *values*  Each key maps to a single value.
#
#  A dictionary is just an extension of this, except that instead of requiring the keys to
#     be consecutive integers starting at 0, we can have *arbitrary* keys!
#
#
# Suppose that a vet has a system where each type of animal gets a ID code:
# '123a' -> 'dog'
# '67xyz' -> 'cat'
# 'yz16' -> 'horse'

# Then, we could  refer to each animal by its key if we'd like.
#
#  One important point:  The keys themselves must be immutable -- that is they can only be ints, str, floats
#   you cannot use a list or a dictionary as the key in a dictionary.

#  Okay, so now what:
#  The following is a dictionary for our animals:

# animal_dict: Dict[str,str] = {'123a': 'dog', '67xyz': 'cat', 'yz16': 'horse'}

# Notice the syntax -- we use { curly braces } to tell Python what follows is a dictionary
# we separate the key and the value with a colon :

# print(animal_dict['67xyz'])
#print(animal_dict['123a'])

# Run this in the console and type:      animal_dict['yz16']

# Now, type:  animal_dict['123']

# You got an error, since the dictionary does not have a value for that key -- this is like asking for
#    s[6] when s = 'abc'.

##############
# Modifying dictionaries
##############

# You can directly modify the value for a key:
# animal_dict['67xyz'] = 'fish'
# print(animal_dict)

# You can add a new key/value pair:
# animal_dict['34c'] = 'turtle'
# print(animal_dict)
# # You can delete a key / value pair by:
# del animal_dict['67xyz']
#
# print(animal_dict)
#
# # Iterate over all keys using for
#
# for k in animal_dict:
#     print(k)
#     print(animal_dict[k])
#
# # The number of keys in a dictionary is given by len(dictionary_name)
# print(len(animal_dict))
#
# #dictionary_name.keys()  will return a list of all keys in the dictionary
#
# print(animal_dict.keys())
#
# # dictionary_name.values()  will return a list of all values (including any duplicates!)
# animal_dict['34c'] = 'horse'
# print(animal_dict.values())

# to see if a key is in a dictionary, use in:
# print('123a' in animal_dict)
# print('4353' in animal_dict)

######## Important info with dictionaries
# Each key maps to a single value (which can be any one thing -- a str, an int, a float, or even a list
#   or another dictionary!
# It is possible that multiple keys might have the same value, though

# You can easily look up by key.  You cannot look up by value
#  That is, given a key, we can ask the dictionary for its matching value.
#  Given a value, we cannot directly ask the dictionary which key(s) it is associated with



# Now, let's try to do the letter_freq count
#
def list_freq_count(s: str) -> List[float]:
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
#
#
#
#
def dict_freq_count(s: str) -> Dict[str, float]:
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
#

word_file = open('alice.txt','r')
s = word_file.read()
word_file.close()

freq_list = list_freq_count(s)

#freq_dict = dict_freq_count(s)



