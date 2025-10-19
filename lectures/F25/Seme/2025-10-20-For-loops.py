# Remember Project #2 Due *next* Wednesday
#
# Homework -- Lists officially due today
# Quiz on Friday over Lists
#
# If you took any make up quizzes last week, stop by office hours
# and we'll go over them together

#
#
# As context for today: Consider


def str_w(s: str):
    i = 0
    while i < len(s):
        print(s[i])
        i += 1


def lst_w(lst: list[int]):
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1

# What do each of these do?
# How are they similar?
# What mistakes could you make while writing them?

# Compare to:


def str_f(s: str):
    for char in s:
        print(char)


def list_f(lst: list[int]):
    for item in lst:
        print(item)




# Today, we introduce two related ideas
#
# * Iterables -- which we have sort of already seen, but not
# talked about explicitly as "iterables"

# * for loops
#


# Iterables
# An iterable is an object (i.e. something in memory in Python, basically)
# which is itself an ordered collection of members
# where we can access a single member at a time

# Examples:
#  *  a string -- an ordered collection of characters, where we
#             can go through one at a time
#  *  a list -- an ordered collection of items, again we
#             can go through them one at a time
#  *  range -- a new idea:
#
#  range()
#   range is a function which takes at least one, and up to three integer parameters:

# range(n) will create a sequence of integers, 0, 1, 2, ..., (n-1)
#       notice that this contains exactly n entries, and is like the slide [0:n]

# range(k, n) will create the sequence k, k + 1, k + 2, ..., (n - 1)
#       again, we start *at* the first number, and stop *right before* the second
#       this will contain exactly n - k entries -- like [k: n]

# range(k, n, i) will create k, k + i, k + 2i, ..., xx
#       xx ?? What does that mean?
#       xx will be the last integer in this sequence < n.
#       this will contain (n - k - 1) // i entries
#       It starts at k, and goes up by i until it reaches or exceeds n
# range(3, 5, 25) would produce 3, 8, 13, 18, 23

# Essentially, range allows us to turn an integer into an iterable.


###############
# now, for loops

# first, recall while loops

# they are really useful -- but one issue is forgetting to increment the counter
#



# a for loop has the following structure:

# for <variable> in <iterable>:
#   now you have explicit access to each member of <iterable>
#   <variable> loops through the members of <iterable> one at a time

# Benefits:
# no indexing errors or infinite loops
#
# # Costs:
# #  you only have access to the current value of <variable>
# # #

# if you only need access to each member one at a time, for loops are usually best
# if you need access to the index so you can work with more than one
#     part of the iterable:
#       * while loops are often more natural
#       * for loops can still be used, though nearly always with range()
#       * for vs while in this case is often a matter of taste.

# Let's practice:

# Write a function str_count(s: str, c: str) -> int:
# which will count the number of times the character c appears in s

def str_count_while(s: str, c: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] == c:
            count += 1
        i += 1
    return count

def str_count(s: str, c: str) -> int:
    1




# Given a list of strings, add the character '!' to the end of each
def excite(lst: list[str]) -> list[str]:
    1

######

# returns true if c is in s, false otherwise
def string_find(s: str, c: str) -> bool:
    1


# given a list of ints, return True if there are an even number of odd integers
def even_odds(lst: list[int]) -> bool:
    1




### Caution -- you should *NOT* ever adjust the iterable in the loop!

def do_not_do_this(lst):
    for item in lst:
        lst.append(5)

    return lst