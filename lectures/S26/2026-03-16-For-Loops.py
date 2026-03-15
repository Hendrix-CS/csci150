# Reminders
# Homework #7 -- For Loops assigned; due Monday after break
# Quiz #7 - For Loops, Friday after break
#
# Project #2 due Friday, 8:10am
# In class on Friday, we will play everyone's word games *and*
# there will be donuts!
#
#
# Last time

lst = ['hi',' bye','lemur', 'spock', 'computer science']


def excite_while(lst: list[str]):
    i = 0
    while i < len(lst):
        lst[i] += '!'
        i += 1


def excite_for(lst: list[str]):
    for word in lst:
        word += '!'


# the first one acted as we expect, but not the second
#
# in a for loop, the iterating variable (word in this case)
# is not (typically) literally the item in the list
# so changing it does not change the list

def excite_for_better(lst: list[str]):
    1




# now some practice with for loops -- we will likely
# not get through all of these on Monday
# but will simply continue into Wednesday

# sum the first n integers:
def sum_to_n(n: int) -> int:
    1

# how many vowels (aeiou) are in s
def count_vowels(s: str) -> int:
    1

# how many total vowels are in all words in he list
def count_vowels_in_list(lst: list[str]) -> int:
    1


# return True of the list contains more even than odd integers
def more_evens(list: list[int]) -> bool:
    1


# return True if the list is in increasing order
def is_sorted(lst: list[int]) -> bool:
    1


def find_max(lst: list[int]) -> int:
    1


# Warning -- you should not change the length of a list
# while iterating with a for loop
# * do not pop or remove
# * do not append

# given a list of ints, return a new list with only the evens
def even_list(lst: list[int]) -> list[int]:
    1

# given a list of ints, change the list so it only has evens
def even_list_new(lst: list[int]) -> list[int]:
    1

# remove from a list all words which contain the letter 'a'
def remove_a(lst: list[str]):
    1



## Common Loop Patterns

#https://hendrix-cs.github.io/csci150/lectures/loop_recipes