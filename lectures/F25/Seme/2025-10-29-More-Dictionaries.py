# Project #2 Due Now
#
# For loop quiz on Friday


# Reminders: Dictionary Homework due Monday
#



# Dictionary Examples --

# Given a list of distinct strings, each string is the key and the value
# is the number of 't's in the string
def t_count(lst: list[str]) -> dict[str,int]:
    return_dict  = {}
    for item in lst:
        c = item.count('t')
        return_dict[item] = c

    return return_dict



# for each integer 0, 1, ..., n:
# the key is the integer and the value is the
# number of times you need to //2 to get 0

def div_count(n: int) -> dict[int,int]:
    div_dict = {}
    i = 0
    while i <= n:
        count = 0
        num = i
        while num > 0:
            num = num // 2
            count += 1

        div_dict[i] = count

        i += 1



    return div_dict


# given a string, use .split() to separate into individual words
# and return a dictionary with the keys the individual words
# and value the number of occurrences of that word
def word_freq(s: str) -> dict[str,int]:
    1


# The user will enter  words
# Each word will do into a dictionary, keyed on word length, with value the list
#   of words of that length
#
# We will exit when the user enters the word 'Exit'

def word_count() -> dict[int, list[str]]:
    1
#
#
# value_find():
# Suppose you have a dictionary d, which has keys which are strings and
# values a list of integers
#
# Given a particular integer n, we want to return a list of the keys
# for which n belong to their value:
#
# For example:
# d = {'a': [5, 1, 2, 3], 'b': [1, 2, 3, 4], 'c': [2, 4, 2], 'd': [1, 3, 5]}
# then value_find(d, 3) would return ['a', 'b', 'd'] and
# value_find(d, 2) would return ['a', 'b', 'c'] and
# value_find(d, 7) would return []

def value_find(d: dict[str, list[int]], n: int) -> list[str]:
    1


# dict_reverse():
# Given a dictionary d, with keys ints and values strings,
# return a dictionary whose keys are the strings and values
# the *list* of integers that matched them
#
# (note why we need a list -- it is possible that multiple
# distinct ints match to the same string)

def dict_reverse(d: dict[int, str]) -> dict[str: list[int]]:
    1


