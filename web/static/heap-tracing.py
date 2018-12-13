from typing import *

## This is an example to use to follow tracing with the Heap
## The Heap will contain any lists and dictionaries that are built,
## as their variables are references to the object.  The variables names
## themselves still go in the stack, with an arrow to the Heap.
## Strings, ints, floats will go in the stack

## List version
## change_list will add a few values to a list
def change_list(lst: List[int]) -> List[int]:
    for i in range(4):
        lst.append(i**2)

    lst.append(42)

    return lst

def main():
    mylist : List[int] = [0,5,-2,8]
    print(mylist)
    templist : List[int] = mylist
    print("Change: ", change_list(templist))
    print(mylist)
    templist[1] = -17
    print(mylist)

main()

## String Version
## This works differently.  Since strings are immutable, any time a string
## is modified, a new instance of the string is created.

def change_string(s : str) -> str:
    for i in range(4):
        s += str(i**2)

    s += '42'

    return s

def main1():
    mystring : str = 'abcd'
    print(mystring)
    tempstring : str = mystring
    print("Change: ", change_string(tempstring))
    print(mystring)
    ## We cannot write an equivalent to templist[1] = -17,
    ## since we cannot individually change the value of a single character
    ## in a string



main1()
