# While loop practice!
# 30 September, 2015

def int_input(prompt):
    """Prompt the user for an integer
    using the given prompt, and repeat
    until they enter a valid integer.
    """

    valid = False
    while not valid:
        s = raw_input(prompt)
        if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
            valid = True
        else:
            print s + " is not a number.  Try again."

    return int(s)

##    s = ""
##    while not s.isdigit():
##        s = raw_input(prompt)
##        if not s.isdigit():
##            print s + " is not a number.  Try again."
##
##    return int(s)

## Recall the Collatz Conjecture

def hailstone(n):
    """Compute the hailstone function of n:
    if n is even, divide by 2; otherwise
    multiply by 3 and add 1.
    """
    
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def collatz(n):
    """Apply the hailstone function to n
    until reaching 1.  Return the number
    of iterations required.
    """

    count = 0
    while n != 1:
        n = hailstone(n)
        # count = count + 1   # increment
        count += 1    # special syntax that means the same thing
        
    return count

def test():
    n = int_input("Enter a number: ")
    print collatz(n)

test()
