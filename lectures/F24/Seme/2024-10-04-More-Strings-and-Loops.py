# Homework -- Function Stack Tracing due Monday

def str_aaa(s: str) -> bool: # return True if s contains at least 3 a's

    count_a = 0
    i = 0

    while i < len(s):
        if s[i] == 'a':
            count_a += 1
            if count_a >= 3:
                return True

        i += 1
    return False

    # if count_a >= 3:
    #     return True
    # else:
    #     return False


###########################
# Input Checking

#Yes/No Response

# returns True if they say yes and False for no
# can deal with YES, yes, y, Y  vs NO, no n, N
# and otherwise reasks
def yes_or_no() -> bool:
    success = False

    while not success:
        ans = input('Please enter yes or no: ')

        if ans.lower() == 'y' or ans.lower() == 'yes':   # yes
            return True
        elif ans.lower() == 'n' or ans.lower() == 'no':   # yes
            return False

        else:
            print('Please just enter yes or no. ')


# checks for integer input, including things like -2
def int_input() -> int:
    success = False
    while not success:
        ans = input('Please enter an integer: ')
        if ans.isdigit():
            return int(ans)
        elif len(ans) > 0 and ans[0] == '-' and ans[1:].isdigit():
            return int(ans)
        else:
            print('Please try again')








# float -- should be able to deal with 5, 5., 5.0, -5, -5., -5.0
def float_input() -> float:
    success = False
    while not success:
        ans = input('Enter a number: ')
        if ans.isdigit():
            return float(ans)

        elif len(ans) > 0 and ans[0] == '-' and ans[1:].isdigit():
            return float(ans)
        elif len(ans) > 0 and ans[0] == '.' and ans[1:].isdigit():
            return float(ans)

        elif len(ans) > 0 and ans[-1] == '.' and ans[:-1].isdigit():
            return float(ans)

