from typing import *

#########
# Given a list of integers, return the product of
# of those integers
def listprod(numbers: List[int]) -> int:
    i = 0
    product = 1
    while i < len(numbers):
        product *= numbers[i]
        i += 1
    return product

#########
# Given a string, return True if it has a double
# letter somewhere, like "oo" or "kk" in bookkeeper
def double_letter(word:str) -> bool:
    c = 0
    while c < len(word) - 1:
        if word[c] == word[c + 1]:
            return True
        c += 1
    return False

#########
# Given a list of integers, return a list of
# the even integers found in the list
def only_evens(mylist: List[int]) -> List[int]:
    final = []
    count = 0
    while count < len(mylist):
        if mylist[count] % 2 == 0:
            final.append(mylist[count])
        count += 1
    return final

print(only_evens([1, 2, 3, 4, 5]))
