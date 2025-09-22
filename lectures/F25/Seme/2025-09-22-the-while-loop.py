# Today - -two topics:
#  * Input/Output (I/O)
# * While Loops

# Input and Output
# We have previously talked about them a bit:
#
# Output:
# print() -- printing to the screen
#
# # print() is pretty smart -- it can take in a string or an int or ...
# print('Hello World')
#
# print(5)
#
# print(True)
#
# print(3.14159)
#
# # But mixing types can be a problem. There is a nice way:
#
#
# # # f-strings   "format strings"
#
# x = 5
# y = 3.14159
# t = True
#
# print(f'The first number is {x}.')
#
# print(f'The second number is {y} and that is {t}.')

# IMPORTANT! print() and return do very different things


# Input -- getting information from the user
# unlike print(), we usually want to capture the value input
# and so need to make a variable assignment
#
# ans = input('Enter your number: ')
# print(f'Your name is {ans}.')
#
# #print(ans + 3)

def num_plus_3() -> int:
    ans = input('Enter your number: ')
    n = int(ans)
    return n + 3



#
# # input always turns whatever is given into a string.
# # you can 'integerize' or 'float-ize' by:
# n = int(ans)
# print(ans + 3)

# Using PyCharm
# Unlike Kaggle, the entire .py file runs
# I am going to do back and functionalize everything we have done do far
# We are now going to write a function that asks the user to enter a number
# If that number is > 100, it will print something
# Otherwise, it will print another message.



def enter_numb():
    ans = input('Please enter a number: ')
    n = int(ans)

    if n > 100:
        print('That number is large!')
    else:
        print('That number is small.')





# using the function in PyCharm
# 2 options
# call directly from the file itself
# use the Console:  Right click (Mac users, 2-finger click); select Run File in the Python Console

# Also notice all of the underlining going on. It catches spelling errors.


# Recall the 5 aspects of an algorithm:
#
#   Input
#   Output
#   Math
#   Conditionals
#   Repetition

# Today, we introduce a method for repetition

# this is the while loop:
# for example:

def while_example() -> int:
    n = 0
    while n < 100:
        ans = input('Please enter a big number: ')
        n = int(ans)

    print(f'Yes, {n} is a big number.')



# In general, it is like an if statement, except that rather than going through the indented
# code only once, it does so until the boolean conditional is false:

# while <boolean>:
#   do some things
#   do some more things

# at the end of each indented block, the code jumps back to the while's conditional statement
# as long as the condition is still true, the while loop executes again
# there is no limit to the number of times that the while loop can execute

def sum_to_n(n: int) -> int:
    s = 0
    cur = 0
    while cur <= n:
        s += cur
        cur += 1
    print(s)

def print_to_n(n):
    cur = 0
    while cur <= n:
        print(cur)
        #cur += 1