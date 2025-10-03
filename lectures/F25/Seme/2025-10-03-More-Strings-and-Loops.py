# Homework #5 -- Strings due Monday


####
# Leftover from Wednesday
def is_inorder(s: str) -> bool:

    i = 0
    while i < len(s) - 1:
        if s[i] > s[i + 1]:

            return False

        i += 1

    return True


# Note the len(s) - 1 above
# When comparing, if the string has 5 characters, we only need to do 4 comparisons
# forgetting the -1 will lead to an index error, which you then fix



def str_aaa(s: str) -> bool: # return True if s contains at least 3 a's

    a_count = 0
    i = 0
    while i < len(s):
        if s[i] == 'a':
            a_count += 1

        i += 1

    if a_count < 3:
        return False
    else:
        return True
















###########################
# Input Checking

#Yes/No Response

# returns True if they say yes and False for no
# can deal with YES, yes, y, Y  vs NO, no n, N
# and otherwise reasks
def yes_or_no() -> bool:

    success = False
    while not success:
        ans = input('Please answer yes or no: ')
        ans = ans.lower()
        if ans == 'yes' or ans == 'y':
            return True
        elif ans == 'no' or ans == 'n':
            return False
        else:
            print('I did not understand. Please try again.')















    success = False

    while not success:
        ans = input('Please enter yes or no: ')

        if ans.lower() == 'y' or ans.lower() == 'yes':   # yes
            return True
        elif ans.lower() == 'n' or ans.lower() == 'no':   # yes
            return False

        else:
            print('Please just enter yes or no. ')


# PLEASE -- looks at the below code before class on Monday.  We'll talk about it then.


# checks for integer input, including things like -2
def int_input() -> int:
    1
    # success = False
    # while not success:
    #     ans = input('Please enter an integer: ')
    #     if ans.isdigit():
    #         return int(ans)
    #     elif len(ans) > 0 and ans[0] == '-' and ans[1:].isdigit():
    #         return int(ans)
    #     else:
    #         print('Please try again')




