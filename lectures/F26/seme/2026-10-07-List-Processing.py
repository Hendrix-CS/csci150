# Reminders
# Quiz #5 - Strings on Friday
# Homework #6 Assigned Today -- Lists, including by hand and CodingBat
# Project #2
# -- Project #2 Work Day this coming Monday in class
# -- Due Friday, October 23


# Recall from lst time that a list is a lot like a string:
# -- an ordered collection of items
# -- we can use indices and slices
# -- we will use while loops to process, one item at a time

def print_char(s: str):
    i = 0
    while i < len(s):
        print(s[i])
        i += 1

# This will go through the string, one character at a time
# and print that character

def print_item(lst: list[int]):
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1

# This will likewise go through the list and print one item at a time

# Let's practice:


# Given a list of integer, return the sum of that list
def list_sum(lst: list[int]) -> int:
    1

# Given a list of string, return how many strings were at least 5 characters long
def long_string(lst: list[str]) -> int:
    1

# Given a list of integers, return a list which contains only the evens
def even_list(lst: list[int]) -> list[int]:
    1

