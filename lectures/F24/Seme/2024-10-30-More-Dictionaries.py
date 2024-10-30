from typing import *


# Reminders: Dictionary Homework due Monday
#



# Dictionary Examples --

# Given a list of distinct strings, each string is the key and the value
# is the number of 't's in the string
def t_count(lst: List[str]) -> Dict[str,int]:
    return_dict  = {}
    for item in lst:
        c = item.count('t')
        return_dict[item] = c

    return return_dict



# for each integer 0, 1, ..., n:
# the key is the integer and the value is the
# number of times you need to //2 to get 0

def div_count(n: int) -> Dict[int,int]:
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

# Same idea a before, except the keys are the
# number of times needed and the value is the
# list of numbers:
def rev_div_count(n: int) -> Dict[int,List[int]]:
    div_dict = {}
    i = 0
    while i <= n:
        count = 0
        num = i
        while num > 0:
            num = num // 2
            count += 1

        if count not in div_dict:
            div_dict[count] = []
        div_dict[count].append(i)



        i += 1




    return div_dict

# The user will enter  words
# Each word will do into a dictionary, keyed on word length, with value the list
#   of words of that length
#
# We will exit when the user enters the word 'Exit'

def word_count() -> Dict[int, List[str]]:
    out_dict = {}  # we need to build a new, empty dictionary

    cont = True  # a flag; will switch to False when the user enters 'Exit'

    while cont:
        ans = input('Please enter a word ("Exit" to stop): ')
        if ans == 'Exit':
            cont = False
        else:
            leng = len(ans) # not required, but easier conceptually for me

            # we want to put this information into the dictionary
            # -- but we do not know if <leng> is currently a valid key!
            # -- this is a common issue when building a dictionary
            if leng not in out_dict:
                out_dict[leng] = []

            out_dict[leng].append(ans)


    return out_dict
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

def value_find(d: Dict[str, List[int]], n: int) -> List[str]:
    return_lst = []
    for k in d:
        if n in d[k]:
            return_lst.append(k)

    return return_lst


