# Reminders
# Project #2 Due Friday
# -- Friday's class is a Demo day -- we'll play each other's word games
# -- requests for extensions must be submitted by class time on Friday

def print_str(s: str):
    i = 0
    while i < len(s):
      print(s[i])
      i += 1

# What does this do?
# If you are writing from scratch, what could go wrong?
# Is there a better way? (Yes!)

def print_str_2(s: str):
    for char in s:
        print(char)

# The for loop
# basic syntax:

# for <variable> in <iterable object>:

# then <variable> will take on, in turn, each value of the things in <iterable object>
#
#
# But what is an <iterable object>?
#
# strings -- an ordered collection of characters
# lists -- an ordered collection of items
# (there are others, which we will encounter later)

def print_list(lst: list[int]):
    for item in lst:
        print(item)

# Though you can use any valid variable name for <variable> in the for loop, I often:
# -- use char for strings
# -- item for lists

# given a list of integers, return the sum
def list_sum(lst: list[int]) -> int:
    total = 0
    for item in lst:
        total += item

    return total


# given a list of strings, only print those whose length is at least 5 characters
def print_long_strings(lst: list[str]):
    for item in lst:
        if len(item) >= 5:
            print(item)



# count characters -- given a string s and character c, count occurrences of c in s
def count_char(s: str, c: str) -> int:
    total = 0
    for char in s:
        if char == c:
            total += 1

    return total



# But, what about something like:
# Given an integer n, print all of the integers, starting at 0, up to  not including n

# As a while loop:
def print_ints(n: int):
    i = 0
    while i < n:
        print(i)
        i += 1

# Can we do this with a for loop?
# Yes!
# We need to turn the integer n into an iterable object
#
# range()

def print_ints_for(n: int):
    for i in range(n):
        print(i)

# range() can take on 3 forms:
#
# range(n) returns the iterable: 0, 1, 2, 3, ..., n - 1
#
# range(a, n) returns the iterable: a, a + 1, a + 2, ..., n - 1
#
# range(a, n, k) returns the iterable: a, a + k, a + 2 * k, a + 3 * k,... and stops before n

def factorial(n: int) -> int:
    total = 1
    for i in range(1,n + 1):
        total *= i

    return total

# But what about:
#
# given a list of ints, return True if they are in increasing order, False otherwise

def is_sorted(lst: list[int]) -> bool:
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False
        i += 1
    return True

# Can we do this with a for loop?
# Yes -- we'll start there on Wednesday






