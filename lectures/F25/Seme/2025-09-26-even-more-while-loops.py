# Today we are going to write one relatively large piece of code:
#
# Recall the Hailstone function, which, given a positive integer n
# either divides by 2 (if n is even) or
# multiplies by 3 and adds 1
#
#
# It is an open question in mathematics, called the Collatz Conjecture,
# whether each starting value of n eventually reaches 1
#













# According to a recent paper, all numbers up to 2^71 (about 2.36 x 10^21)
# do eventually reach 1
# [Barina, David. "Improved verification limit for the convergence of the Collatz conjecture,"
# The Journal of Supercomputing, vol 81, page 810 (2025)]
#
#
# We are going to write a program which:
# Given a value of n will test all positive
# starting values k <= n
# and returns the total number of steps needed to get to 1.

# What do we need to do?
# write the Hailstone Function
# Make a step counter
# Be able to check all numbers up to n
# Ask the user for input value

# Have a main() which controls everything

def print_rules():
    print('This program will ask you for a starting number')
    print('which should be a positive integer.')
    print()
    print('It will then test all values from 1 to that number')
    print('and return the number of steps the Hailstone Function')
    print('needs to reach 1.')
    print()

def get_ending_number():
    success = False
    while not success:
        ans = input('Please enter a positive integer: ')
        if ans.isdigit() and int(ans) > 0:
            n = int(ans)
            success = True
        else:
            print('I did not understand. Please try again.')
    return n

# for check_up_to_n() we need:
# to write Hailstone
# keep track of steps
# print out answer
# go to the next number

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def step_count(n: int) -> int:
    steps = 0
    while n != 1:
        n = hailstone(n)
        steps += 1
    return steps

def check_up_to_n(n: int):
    start = 1
    while start <= n:
        steps = step_count(start)
        print(f'The number {start} takes {steps} steps to reach 1.')
        start += 1






def main():
    print_rules()
    n = get_ending_number()
    check_up_to_n(n)

main()






