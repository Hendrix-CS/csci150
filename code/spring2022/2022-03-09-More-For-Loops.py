from typing import *
# Write functions which




# list_sum - given a list of integers, return the sum. Empty should return 0

#while loop version
# def list_sum(lst: List[int]) -> int:
#     i = 0
#     sum_so_far = 0
#     while i < len(lst):
#         sum_so_far += lst[i]
#         i += 1
#     return sum_so_far

#for loop version
# def list_sum(lst: List[int]) -> int:
#     sum_so_far = 0
#     for item in lst:
#         sum_so_far += item
#     return sum_so_far




#
#
#
#
#
#
#
#
#
#
# # string_find: given a string s, return True if character c is in the string
#
# def string_find(s: str, c: str) -> bool:
#
#     for char in s:
#         if char == c:
#             return True
#
#     return False
#
# def string_find2(s: str, c: str) -> bool:
#     found = False
#     for char in s:
#         if char == c:
#             found = True
#
#     return found
#
#
# def even_string_find(s: str, c: str) -> bool:  # returns True only if s contains an even
#     # number of c's
#
#     # # count method
#     # count = 0
#     # for char in s:
#     #     if char == c:
#     #         count += 1
#     #
#     # return count % 2 == 0
#     #
#     # # if count % 2 == 0:
#     # #     return True
#     # # else:
#     # #     return False
#
#
#     ## flag method
#     flag = True
#
#     for char in s:
#         if char == c:
#             flag = not flag
#
#     return flag
#
#
#
#
#
#
#
# # find -- given a string and character c, return True if c is in string
#
#
#
#
#
# # repeat the above, but for items in a list
# def list_find(lst: List[int], n: int) -> bool:
#     found = False
#     for item in lst:
#         if item == n:
#             found = True
#
#     return found
#
#
#




# given a list of integers, if item is a multiple of seven, replace it with item // 7

def sevens(lst: List[int]) -> List[int]:

    for item in lst:
        if item % 7 == 0:
            item = item // 7

    return lst

# the above does not work -- it does not change the values of anything *in* the list

def sevens2(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        if lst[i] % 7 == 0:
            lst[i] = lst[i] // 7

    return lst

# the above changes lst. What ifd you wanted to leave lst alone?

def sevens3(lst: List[int]) -> List[int]:
    new_list = []
    for item in lst:
        if item % 7 == 0:
            new_list.append(item // 7)
        else:
            new_list.append(item)
    return new_list


# given a list of ints, return a new list with all multiples of seven *removed*

def remove_seven(lst: List[int]) -> List[int]
    new_list = []
    for item in lst:
        if item % 7 != 0:
            new_list.append(item)

    return new_list



# def sevens(lst: List[int]) -> List[int]:
#     for item in lst:
#         if item % 7 == 0:
#             item = item // 7
#     return lst
#
# this does not work since it does not affect the list itself
#
#
# def sevens2(lst: List[int]) -> List[int]:
#     for i in range(len(lst)):
#         if lst[i] % 7 == 0:
#             lst[i] = lst[i] // 7
#     return lst
#


# what if you wanted to only keep those that are a multiple of 7?

#def keep_sevens(lst: List[int]) -> List[int]:

# given a string, if a character is 'e', replace it with 'E'


#### for loops -- important
# inside a for loop, you should not change either the value of the
# looping variable itself, nor the iterable that is being looped over!