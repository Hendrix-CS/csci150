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