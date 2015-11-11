# CSCI 150
# Lab 11: Die Hard III

######################################################################
# Below are some utility functions you may use in implementing the
# WaterJug game.  We are providing them because you already know how
# to write functions like this, and we want you to focus on other
# aspects of the lab.
#
# Note you are not required to use these functions, and you may change
# them if you wish.  They are provided for convenience only.
######################################################################

def try_again(msg):
    print msg + " Try again."

def int_input(prompt):
    """Keep prompting the user until they enter a valid positive
    integer."""

    valid = False
    while not valid:
        s = raw_input(prompt)
        if s.isdigit():
            valid = True
        else:
            try_again(s + " is not an integer.")

def show_options(options):
    """Present the user with a list of options."""

    print "Your options:"
    i = 0
    for opt in options:
        i += 1
        print "  " + str(i) + ") " + opt

def range_input(lo, hi, prompt):
    """Prompt the user to enter a number between lo and hi, inclusive.
    For example,  range_input(6,10,"How many wibbles? ")  will keep
    asking the user "How many wibbles? " until they enter a valid
    number between 6 and 10.  This function is also useful for
    allowing the user to pick one of several numbered options."""

    valid = False
    while not valid:
        choice = int_input(prompt)
        valid = lo <= choice and choice <= hi
        if not valid:
            print "That is not a valid choice.  Please enter a number from " + str(lo) + "-" + str(hi) + "."

    return choice

############################################################

class WaterJug:

    # Remove "pass" and implement me!
    pass



def main():

    options_list = [ "Fill a jug", "Empty a jug", "Pour", "Give up" ]

    print "Implement me!"


main()
