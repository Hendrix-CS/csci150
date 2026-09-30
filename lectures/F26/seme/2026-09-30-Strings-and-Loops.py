# Reminders
# * Project #1 -- Due Now
# * Homework #5 -- Assigned today (Strings)
# * Quiz #4 -- Friday (While Loops)
#
#
# Last week we wrote the following:

def enter_integer() -> int:
    success = False

    while not success:
        ans = input('Enter an integer: ')
        if (ans.isdigit()) or (ans[0:1] == '-' and ans[1:].isdigit()):
            num = int(ans)
            success = True
        else:
            print('I did not understand. Please try again.')

    return num

# This was nice, but did not work for negatives, since the '-' symbols messes up .isdigit()
# Let's fix this!

# Looping over a string s
#
# i = 0
#
# while i < len(s):
#
#     i += 1

# Given a string, count the number of digits:  'hello 5 1 ! @ jhf 7' should return 3
def count_digits(s: str) -> int:
    i = 0
    number = 0

    while i < len(s):
        if s[i].isdigit():
            number += 1

        i += 1

    return number

def count_char(s: str, c: str) -> int:
    i = 0
    number = 0
    while i < len(s):
        if s[i] == c:
            number += 1

        i += 1

    return number


# We cannot change a character of a string 'in place' in a loop
# We also should not modify a string while looping over it

def remove_char(s: str, c: str) -> str:  # return string with all occurances of c removed
    i = 0
    out_str = ''
    while i < len(s):
        if s[i] != c:
            out_str += s[i]

        i += 1

    return out_str

def replace_char(s: str, c: str, d: str) -> str:  # replace  all c with d
    i = 0
    out_str = ''
    while i < len(s):
        if s[i] != c:
            out_str += s[i]
        else:
            out_str += d

        i += 1

    return out_str



def in_alpha_order(s: str) -> bool: # returns True if the string's characters are in abc order
    i = 0

    while i < len(s) - 1:
        if s[i] > s[i + 1]:
            return False

        i += 1

    return True

