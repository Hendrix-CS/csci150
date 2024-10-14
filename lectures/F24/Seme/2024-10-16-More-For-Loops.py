from typing import *
# Project #2 Due Next Friday!
# CodingBat homework on loops and lists due Monday
#   -- for the homework, you can either use while or for as you see fit



# Coding Bat: Sample
def sum67(nums):
    sum = 0
    flag = True
    i = 0
    while i < len(nums):
        if nums[i] == 6:
            flag = False
        elif flag:
            sum += nums[i]
        elif nums[i] == 7:
            flag = True
        i += 1
    return sum


# Write functions which


#
#
#

# given a list of integers, if item is a multiple of seven,
# replace it with item // 7

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

def sevens4(lst: List[int]) -> List[int]:
    new_list = lst
    for i in range(len(new_list)):
        if new_list[i] % 7 == 0:
            new_list[i] = new_list[i] // 7
    return new_list


# given a list of ints, return a new list with all multiples of seven *removed*

def remove_seven(lst: List[int]) -> List[int]:
    new_list = []
    for item in lst:
        if item % 7 != 0:
            new_list.append(item)

    return new_list




#### for loops -- important
# inside a for loop, you should not change either the value of the
# looping variable itself, nor the iterable that is being looped over!**

# ** It is ok to change an individual value in a list,
# ** do not change a string "in place" as you loop over the string

## Common Loop Patterns

https://hendrix-cs.github.io/csci150/lectures/loop_recipes
