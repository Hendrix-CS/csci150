# Remember to starting thinking about Project #2
# Homework -- CodingBat -- Lists and Loops - Due next Monday
# Quiz on Wednesday over Function Stack Tracing
# Also, make-up Quiz on While Loops on Wednesday


from typing import *

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
#       notice that this contains exactly n entries, and  like a slice
#       starts at 0, but ends at n - 1

# range(k, n) will create the sequence k, k + 1, k + 2, ..., (n - 1)
#       again, we start *at* the first number, and stop *right before* the second
#       this will contain exactly n - k entries

# range(k, n, i) will create k, k + i, k + 2i, ..., xx
#       xx ?? What does that mean?
#       xx will be the last integer in this sequence < n.
#       this will contain (n - k - 1) // i entries

# Essentially, range allows us to turn an integer into an iterable.


###############
# now, for loops

# first, recall while loops

# they are really useful -- but one issue is forgetting to increment the counter
#
# s = 'abcde'
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# the for loop avoids that

# compare:

# s = 'abcdef'
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
# #
# s = 'abcdef'
# for char in s:
#     print(char)


# a for loop has the following structure:

# for <variable> in <iterable>:
#   now you have explicit access to each member of <iterable>
#   <variable> loops through the members of <iterable> one at a time

# Benefits:
# no indexing errors or infinite loops

# Costs:
#  you only have access to the current value of <variable>
# #
# s='abcdef'
# i = 0
# while i < len(s):
#     print(i, s[0:i])
#     i += 1
#
#
# s = 'abcdef'
# index = 0
# word = ''
# for char in s:
#     print(index, word)
#     index += 1
#     word += char
# #
# # We can't do this by using 'char' in s
#
# s = 'abcdef'
# for i in range(len(s)):
#     print(i, s[0:i])

# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i+2])
# if you only need access to each member one at a time, for loops are always best
# if you need access to the index so you can work with more than one
#     part of the iterable:
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
    count = 0
    for char in s:
        if char == c:
            count += 1

    return count




# Given a list of strings, add the character '!' to the end of each
def excite(lst: List[str]) -> List[str]:
    new_list = []
    for word in lst:
        new_list.append(word +'!')

    return new_list
#
def excite2(lst: List[str]) ->List[str]:
    for i in range(len(lst)):
        lst[i] += '!'

    return lst

def excite3(lst: List[str]) -> List[str]:
    for word in lst:
        word += '!'
    return lst

######

def string_find(s: str, c: str) -> bool:
    1

# given a list of ints, return True if there are an even number of odd integers
def even_odds(lst: List[int]) -> bool:
    1