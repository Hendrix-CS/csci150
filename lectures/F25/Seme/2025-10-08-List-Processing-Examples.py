## Note to Lars -- from typing import *
# Not needed: Lower Case List




# Reminder from last time
# join() -- the opposite of split:  str.join(list) will return a string with the value of str between each entry
# only works if the original list is made up of string entries
#
# print(';'.join(['Hi','there','how','are','you?']))
# #
# lst = ['dog','log','lot','tot']
# print('->'.join(lst))
# #
# # # The newline character   \n
# # s = '\n'
# # print(len(s))
# #
# # print('Hello, how are \n you today?')
#
#
# print('\n'.join(lst))
#'dog\nlog\nlot\ntot\n'
# List processing:

# given a list of integers, return their sum
def list_sum(lst: list[int]) -> int:
    s = 0
    i = 0
    while i < len(lst):
        s += lst[i]
        i += 1

    return s


# given a list of integers, return their product
def list_prod(lst: list[int]) -> int:
    p = 1
    i = 0
    while i < len(lst):
        p *= lst[i]
        i += 1

    return p






# given a list of integers, lst, and a single integer n,
# count how many integers in lst are smaller than n
def small_count(lst: list[int], n: int) -> int:
    c = 0

    i = 0
    while i < len(lst):
        if lst[i] < n:
            c += 1
        i += 1

    return c





















# given a list of strings and a character, return a count of the number of strings (i.e. items in the list)
# which contain at least one occurrence of the character.

new_list = ['apples','bananas','pears','oranges','tangerines']

def count_occur(lst: list[str], s: str) -> int:
    c = 0
    i = 0
    while i < len(lst):
        if s in lst[i]:
            c += 1
        i += 1

    return c




# given a list of strings, each of which is a single lower case word,
# return True if the list is in alphabetical order

def alpha_order(lst: list[str]) -> bool:

    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False

        i += 1

    return True
















# given a list of integers, return a new list which each element tripled
def triple_list(lst: list[int]) -> list[int]:
    new_list = []
    i = 0
    while i < len(lst):
        new_list.append(lst[i] * 3)

        i += 1

    return new_list


