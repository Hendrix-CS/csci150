from typing import *

def explode(lst: List[str]):
    i: int = 0
    while i < len(lst):
        print(lst[i])
        i += 1

# Alternatively:
def explode2(lst: List[str]):
    for s in lst:
        print(s)

# General syntax:
#
# for <new variable> in <list or string expression>:
#    ... stuff using the new variable ...

# for c in 'hello world':
#     print(c)

# Count how many times the character c occurs in the string s.
# e.g.
#   count('lemon', 'w') -> 0
#   count('lemon', 'm') -> 1
#   count('aardvark', 'a') -> 3
def count(s: str, c: str) -> int:
    n: int = 0
    for x in s:
        if x == c:
            n += 1

    return n

# Find the first index of the character c in the string s,
# or -1 if it's not found.
#
# e.g.
#   find('lemon', 'm') -> 2
#   find('aardvark, 'a') -> 0
#   find('aardvark, 'v') -> 4
#   find('aardvark, 'z') -> -1
# def find(s: str, c: str) -> int:
#     for x in s:
#         if x == c:
            # Doesn't work because we don't know what index x came from.

def find(s: str, c: str) -> int:
    for i in range(len(s)):
        if s[i] == c:
            return i

    return -1

# Find the indices of all occurrences of the character c in the string s.
# e.g.
#   find_all('aardvark', 'a') -> [0, 1, 5]
#   find_all('lemon', 'm')    -> [2]
#   find_all('lemon', 'z')    -> []
def find_all(s: str, c: str) -> List[int]:
    indices: List[int] = []
    for i in range(len(s)):
        if s[i] == c:
            indices.append(i)

    return indices



foods = ['pasta', 'sushi', 'pizza', 'pancakes']

for f in foods:
    f += '!'   # This only changes the local variable f,
               # it does not change the list 'foods' at all.

# This works:
# excited = []
# for f in foods:
#     f += '!'
#     excited.append(f)
# foods = excited

# Keeps adding more ! forever:
# for f in foods:
#     f += '!'
#     foods.append(f)

for i in range(len(foods)):
    foods[i] += '!'


# Say whether nums is sorted from smallest to biggest
#
# e.g.  is_sorted([1,2,5,8,23]) -> true
#       is_sorted([1,2,2,2,3,3]) -> true
#       is_sorted([1,2,6,4,9])  -> false
def is_sorted(nums: List[int]) -> bool:




