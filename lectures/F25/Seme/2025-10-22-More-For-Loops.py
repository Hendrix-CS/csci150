# Project #2 Wednesday, October 29!!




# Coding Bat: Sample
def sum67(nums):
    1


# Write functions which


#
#
#

# given a list of integers, if item is a multiple of seven,
# replace it with item // 7

def sevens(lst: list[int]) -> list[int]:
    for item in lst:
        if item % 7 == 0:
            item = item // 7
    return lst






# the above does not work -- it does not change the values of anything *in* the list

def sevens2(lst: List[int]) -> List[int]:
    1

# the above changes lst. What ifd you wanted to leave lst alone?

def sevens3(lst: List[int]) -> List[int]:
    1







#### for loops -- important
# inside a for loop, you should not change either the value of the
# looping variable itself, nor the iterable that is being looped over!**

# ** It is ok to change an individual value in a list,
# ** do not change a string "in place" as you loop over the string

## Common Loop Patterns

#https://hendrix-cs.github.io/csci150/lectures/loop_recipes
