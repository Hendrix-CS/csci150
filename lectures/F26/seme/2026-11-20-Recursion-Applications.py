from dataclasses import dataclass
from datetime import datetime

# No Quiz Today
#
# Last time we saw a nice example of a tree
#   -- which is a simple recursive data structure
#
#
# In some parts of CS, we care a lot about efficiency
# We saw a (bad) example of this on Monday:

def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_timer(n: int):
    for k in range(10, n):
        st = datetime.now()
        f = fib(k)
        et = datetime.now()

        print(f'{f};{k};{(et-st).total_seconds()}')


# Ok, so this method for finding Fibonacci is pretty inefficient.

# But it turns out that some recursive ideas are *really* fast:
# -- binary search (using a tree!)
# -- many sorting algorithms
#     -- merge sort
#     -- quick sort
#  (show 151 lab results)
#
#       -- many built in sorting methods are really
#           a combination of multiple methods

# Python takes care of a lot of these ideas behind the scenes
# It (mostly) makes good choices, but sometimes
# does things kind of inefficiently for the sake of ease of use
# Lists are a primary example
# A List is what you want if you want to be able to
#  -- add to any position
#  -- remove from any position
# -- you are not going to try to maintain it sorted

