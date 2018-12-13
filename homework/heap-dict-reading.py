from typing import *

## Problem 1 -- Trace the execution of this code
## using both the Stack and Heap

def alice(lst : List[int],n : int) -> List[int]:

    len_lst : int = len(lst)
    for i in range(len_lst):
        lst[i] = lst[i] % n

def bob(lst: List[int]) -> str:
    s = ''
    letters: List[str] = ['t','e','a','h','p','!','s','y']
    for num in lst:
        s += letters[num]

    return s



def main():

    mylist = [3,25,14,-2,5]
    alice(mylist,6)
    print(bob(mylist))

main()

## Problem 2 -- trace this code as well

def harry(s: str)-> Dict[str,int]:
    return_dict = {}
    for char in s:
        return_dict[char] = s.find(char)

    return return_dict

def hermione(s: str, in_dict: Dict[str,int]) -> Dict[str,int]:
    for char in s:
        if char in in_dict:
            in_dict[char] += s.count(char)
        else:
            in_dict[char] = -5

    return in_dict

def main1():
    s = 'privet drive'

    main_dict = harry(s)
    new_dict = hermione('george',main_dict)
    new_dict['v'] = 200

    for key in main_dict:
        print(key,main_dict[key])

main1()

