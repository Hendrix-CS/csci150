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
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return total


def list_sum_evens(lst: list[int])->int:
    total = 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            total += lst[i]
        i += 1
    return total






# Given a list of string, return how many strings were at least 5 characters long
def long_string(lst: list[str]) -> int:
    total = 0
    i = 0
    while i < len(lst):
        if len(lst[i]) >= 5:
            total += 1

        i += 1

    return total



# Given a list of integers, return a list which contains only the evens
def even_list(lst: list[int]) -> list[int]:
    return_lst = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            return_lst.append(lst[i])
        i += 1

    return return_lst



# Repeatedly ask the user for an integer.
# Whenever they enter 0, stop and return a list of the numbers they entered

def ask_for_numbs() -> list[int]:
    return_lst = []
    cont = True

    while cont:
        n = int(input('Please enter an integer (0 to stop): '))

        if n == 0:
            cont = False
        else:
            return_lst.append(n)


    return return_lst




s = 'cat->cot->cog->dog'

t = s.split('->')   # .split(delimiter) will return a list, splitting on delimiter
print(t)

t = s.split(';')
print(t)

lst = ['cat', 'cot', 'cog', 'dog']
t = '->'.join(lst)

print(t)






