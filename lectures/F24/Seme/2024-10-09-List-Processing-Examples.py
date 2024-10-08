from typing import *

# #split() - given a string and a character (or sequence of characters),
# returns a list, split on the character.
# s = 'Fred,Daphne,Velma,Shaggy,Scooby-Doo'
# s_list = s.split(',')
# print(s_list)
# # #
# words = 'dog->dot->lot->let'
# print(words.split('->'))
# #
# #
# # # join() -- the opposite of split:  str.join(list) will return a string with
# the value of str between each entry
# # # only works if the original list is made up of string entries
# #
# new_list = ['apples','bananas','pears','oranges','tangerines']
# new_string = '; '.join(new_list)
# print(new_string)
#
#
#
# word_list =  ['dog']
# word_list.append('dot')
# word_list.append('lot')
# word_list.append('let')
# print(word_list)
# print('->'.join(word_list))


# List processing:

# given a list of integers, return their sum
def list_sum(lst: List[int]) -> int:
    i = 0
    our_sum = 0
    while i < len(lst):
        our_sum += lst[i]
        i += 1
    return our_sum


# given a list of integers, return their product
def list_prod(lst: List[int]) -> int:
    1


# given a list of integers, lst, and a single integer n,
# count how many integers in lst are smaller than n
def small_count(lst: List[int], n: int) -> int:
    1

# given a list of strings and a character, return a count of the number of strings (i.e. items in the list)
# which contain at least one occurrence of the character.

new_list = ['apples','bananas','pears','oranges','tangerines']

def count_occur(lst: List[str], s: str) -> int:
    1




# given a list of strings, each of which is a single lower case word,
# return True if the list is in alphabetical order

def alpha_order(lst: List[str]) -> bool:
    1




# given a list of integers, return a new list which each element tripled
def triple_list(lst: List[int]) -> List[int]:
    1



# write app_or_rem(lst: List[str], s: str) -> List[str]
# given a list of strings, lst, and a string, s
# return a new list where:
#  -- if s was not in lst, s should be appended
#  -- if *was* in lst, then s should be removed
#
# for example:
# lst = ['dog','cat','fish'] and s = 'turtle'
# would return ['dog','cat','fish', 'turtle']
#
# but
# lst = ['dog','cat','fish'] and s = 'cat'
# would return ['dog','fish']