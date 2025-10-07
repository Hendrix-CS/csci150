## Note to Lars -- from typing import *
# Not needed: Lower Case List




# Reminder from last time
# join() -- the opposite of split:  str.join(list) will return a string with a the value of str between each entry
# only works if the original list is made up of string entries

print(';'.join(['Hi','there','how','are','you?']))
#
lst = ['dog','log','lot','tot']
print('->'.join(lst))

# The newline character   \n
print('\n'.join(lst))

# List processing:

# given a list of integers, return their sum
def list_sum(lst: list[int]) -> int:
    i = 0
    our_sum = 0
    while i < len(lst):
        our_sum += lst[i]
        i += 1
    return our_sum


# given a list of integers, return their product
def list_prod(lst: list[int]) -> int:
    1


# given a list of integers, lst, and a single integer n,
# count how many integers in lst are smaller than n
def small_count(lst: list[int], n: int) -> int:
    1



# given a list of strings and a character, return a count of the number of strings (i.e. items in the list)
# which contain at least one occurrence of the character.

new_list = ['apples','bananas','pears','oranges','tangerines']

def count_occur(lst: list[str], s: str) -> int:
    1




# given a list of strings, each of which is a single lower case word,
# return True if the list is in alphabetical order

def alpha_order(lst: list[str]) -> bool:
    1















# given a list of integers, return a new list which each element tripled
def triple_list(lst: list[int]) -> list[int]:
    1


