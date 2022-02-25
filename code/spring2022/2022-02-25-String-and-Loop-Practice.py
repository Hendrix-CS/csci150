# Reminders:
# Homework #4 (Function Stack Tracing) &
# Exam #1 Redos are now due on Monday, 2/28

# Project #1 is due next Friday, 3/4

# While Loop Practice
# Write a function sum_to which takes in a single non-negative integer
# n and returns the sum 0 + 1 + 2 + ... + (n)

def sum_to(n: int) -> int:
    sum_so_far = 0
    i = 0
    while i <= n:
        sum_so_far += i
        i += 1

    return sum_so_far


# Consider the following code:

# What happens if we call string_counter('hendrix','m') ?
def string_counter(s: str, t: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] < t:
            count += 1
        i += 1
    return count

# While loops and strings

# i = 0
# while i < len(s):
#   do stuff
#   i += 1




# Example -- 'Explode' string -- given a string, print each
#of its characters, one at a time to the screen

def explode_str(s: str):
    i = 0
    while i < len(s):
        print(s[i])
        i += 1


# Now, let's try something new -- reverse a string
# that is, given a string s = 'abcde', we want to return 'edcba'










def reverse(s: str) -> str:
    i = 0
    return_str = ''
    while i < len(s):
        return_str = s[i] + return_str
        i += 1

    return return_str



# Write is_inorder(s: str) -- will take in a lower case word
# and return True if the characters all appear in alphabetical order
# repeated letters are ok:
# 'hiss' is True, as is 'art', but 'sleet' is False



def is_inorder(s: str) -> bool:

    i = 0
    while i < len(s) - 1: # we need the -1 here since we do not need to check the last character against the next -- since there is not one!
        if s[i] > s[i+1]:
            return False
        i += 1
    return True

















# def reverse(s: str) -> str:
#     i = 0
#     return_str = ''
#     while i < len(s):
#         return_str = s[i] + return_str
#         i += 1
#
#     return return_str


# new int_input

def int_input(prompt: str) -> int:
    is_okay = False
    while not is_okay:
        answer = input(prompt)
        if answer.isdigit():
            is_okay = True
        elif answer[0] == '-' and answer[1:].isdigit():
            is_okay = True
        else:
            print('That is not a valid integer. Please try again.')

    return int(answer)