from dataclasses import dataclass
from datetime import datetime
import random

# No Quiz Today
#
# Note: Today is not about the code, but the ideas
# -- do not worry if you get a bit lost trying to read the code!
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


# Here is a much faster one that does not use recursive.  It is a straight
# forward bottom-up version

def fast_fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    prev_2 = 1
    prev_1 = 1
    k = 2
    while k < n:
        new = prev_2 + prev_1
        prev_2 = prev_1
        prev_1 = new
        k += 1
    return prev_2 + prev_1

def fast_fib_timer(n: int):
    for k in range(10, n):
        st = datetime.now()
        f = fast_fib(k)
        et = datetime.now()

        print(f'{f};{k};{(et-st).total_seconds()}')

# But it turns out that some recursive ideas are *really* fast:
# -- binary search (using a tree!)
# -- many sorting algorithms
#     -- merge sort
#     -- quick sort

#
#       -- many built in sorting methods are really
#           a combination of multiple methods


# Sorting -- given a list, sort it into increasing order.
# There are a lot of sorting algorithms.
# We will look at 3:
# -- bubble sort -- push the largest value to the top of the list
#       * non-recursive
#       * easy to program


def bubble_sort(lst: list[int]) -> list[int]:
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:  # we swap
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
    return lst


# -- merge sort -- divide and conquer
#       * split list in half
#       * sort each half (by using merge sort!)
#       * merge the results together
#       * recursive!



def merge(left: list[int], right: list[int]) -> list[int]:
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list += left[i:]
    sorted_list += right[j:]

    return sorted_list

def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst

    else:
        center = len(lst) // 2  # where to split
        left = merge_sort(lst[:center])
        right = merge_sort(lst[center:])

        return merge(left,right)


# -- built-in Python sorted() method
#     * formally is a "meta" method
#     * does work behind the scenes to determine best algorithm to use
#     * is precompiled

def python_sort(lst: list[int]) -> list[int]:
    return sorted(lst)


def random_list(n: int) -> list[int]:
    lst = list(range(n))
    random.shuffle(lst)
    return lst

def sort_time(k: int):
    n = int(input('How long should your list be? (0 to quit)? '))
    while n > 0:
        st = datetime.now()
        print('Creating list')
        lst = random_list(n)
        b_list = lst[:]
        m_list = lst[:]
        p_list = lst[:]

        et = datetime.now()
        print(f'List created in {(et-st).total_seconds()} seconds')

        input('Enter to Sort: ')

        if k != -1:
            st = datetime.now()
            bubble_sort(b_list)
            et = datetime.now()
            print(f'Bubble Sort {n} items time:  {(et-st).total_seconds()}')

        st = datetime.now()
        merge_sort(m_list)
        et = datetime.now()
        print(f'Merge Sort {n} items time:  {(et - st).total_seconds()}')

        st = datetime.now()
        python_sort(p_list)
        et = datetime.now()
        print(f'Python Sort {n} items time:  {(et - st).total_seconds()}')

        n = int(input('How long should your list be? (0 to quit)? '))

#  (show 151 lab results)


