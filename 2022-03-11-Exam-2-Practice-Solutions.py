## Solutions to the Coding parts of Exam #2 Practice

# It is possible that there are other ways to work these, of course

from typing import *

###############################
## In - Class
##############################

# Solutions to the tracing problems can be found linked on the course webpage

#4
def same_char(s: str, t: str) -> int:
    i = 0
    count = 0
    while i < len(s):
        if s[i] == t[i]:
            count += 1
        i += 1

    return count

# 5
def positive_only(lst: List[int]) -> List[int]:
    new_list = []
    i = 0
    while i < len(lst):
        if lst[i] > 0:
            new_list.append(lst[i])
        i += 1
    return new_list

####################################
#### Take - Home
####################################

#1
def word_count() -> int:
    cont = True
    count = 0
    while cont:
        inp = input("Please enter a word ('exit' to quit): ")
        if inp == 'exit':
            cont = False
        else:
            count += 1
    return count

# 2
def my_replace(s: str, t: str, u: str) -> str:
    i = 0
    new_str = ''
    while i < len(s):
        if s[i] == t:
            new_str += u
        else:
            new_str += s[i]
        i += 1
    return new_str

#3
def suffix_to_prefix(s: str, n: int) -> str:
    return s[-n:] + s[:-n]

#4
def sum_between(a: int, b: int) -> int:
    sum_so_far = 0
    i = a
    while i <= b:
        sum_so_far += i
        i+= 1
    return sum_so_far

#5
def make_numb(lst: List[int]) -> int:
    num_str = ''
    i = 0
    while i < len(lst):
        num_str += str(lst[i])
        i += 1
    return int(num_str)

#5 (alternate solution)
def make_numb2(lst: List[int]) -> int:
    numb = 0
    i = 0
    while i < len(lst):
        numb += lst[i] * 10 ** (len(lst)  - i-1)
        i += 1
    return numb

#6
def list_min(lst: List[int]) -> int:
    ind = 0
    i = 0
    while i < len(lst):
        if lst[i] < lst[ind]:
            ind = i
        i += 1
    return ind