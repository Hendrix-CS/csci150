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
        ans = input('Enter a positive integer: ')
        if ans.isdigit():
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
    1


# We cannot change a character of a string 'in place' in a loop
# We also should not modify a string while looping over it

def remove_char(s: str, c: str) -> str:  # return string with all occurances of c removed
    1



def in_alpha_order(s: str) -> bool: # returns True if the string's characters are in abc order
    1

