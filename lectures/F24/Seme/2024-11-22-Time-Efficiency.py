from typing import *
from datetime import datetime
import random

import itertools


# directly below is a new library, which can provide
# a progress bar for loops

from tqdm import tqdm



# The Fibonacci Sequence:  F(0) = 1, F(1) = 1, F(n) = F(n-1) + F(n-2)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n,d):
    d[0] = 1
    d[1] = 1
    if n not in d:
        d[n] = fib2(n-1,d) + fib2(n-2,d)
    return d[n]

def time_compare():

    for n in [5, 10, 15, 20, 25, 30, 35, 40]:
        temp = [n]
        st = datetime.now()
        temp.append(fib(n))
        temp.append(str(datetime.now() - st))


        st = datetime.now()
        temp.append(fib2(n,{}))
        temp.append(str(datetime.now() - st))
        print(temp)



#time_compare()

def time_compare2():

    for n in [100, 200, 300, 400, 500, 900]:
        temp = [n]
        # st = datetime.now()
        # temp.append(fib(n))
        # temp.append(str(datetime.now() - st))


        st = datetime.now()
        temp.append(fib2(n,{}))
        temp.append(str(datetime.now() - st))
        print(temp)
#time_compare2()

# Program Time Efficiency

# One of the fundamental ideas in Computer Science
# is that of "Time Efficiency"
#
# For an input of size n, how long does the program take to run?
# Typically, what we really want to know is not the literal number of seconds
# but instead, if, for example, we doubled n, what happens to time?

# In a linear situation, if we go from n to 2 * n,
# the time also should (roughly) double

# FOr each of the following, you can choose a value of n
# THe program will run and calculate the total time needed

# Adds up the numbers from 1 to n
def linear_sum(n: int):
    st = datetime.now()
    sum_so_far = 0
    for i in tqdm(range(n + 1)):
        sum_so_far += i

    print(datetime.now() - st)
    return sum_so_far

# Searches in a list --
# It makes a random list and then
# searches through that list 2000 times
def linear_search(n: int):
    lst = [random.randint(0, 10 * n) for i in range(n)]
    print('Go!')
    count = 0
    st = datetime.now()
    for times in tqdm(range(2000)):
        test = random.randint(0, 10 * n)
        if test in lst:
            count += 1

    print(datetime.now() - st)
    return count

# Same idea -- but uses the built in idea of a 'set'
# A set is a more efficient way to keep information
# but loses the order in which items were added
def linear_search_set(n: int):
    lst = set([random.randint(0, 10 * n) for i in range(n)])
    print('Go!')
    count = 0
    st = datetime.now()
    for times in tqdm(range(2000)):
        test = random.randint(0, 10 * n)
        if test in lst:
            count += 1

    print(datetime.now() - st)
    return count


# This uses the tree idea we built last time
# Almost all of the work is building the tree -- search is easy
def bst_search(n: int):
    lst = [random.randint(0, 10 * n) for i in range(n)]
    count = 0
    print('Go!')
    st = datetime.now()
    r = bst_list(lst)
    print('Tree Built')
    tt = datetime.now()
    for times in tqdm(range(2000)):
        test = random.randint(0, 10 * n)
        if search(r, test):
            count += 1
    print(f'Total: {datetime.now() - st}  Search: {datetime.now() - tt}')


# Now a helper function for sorting
def list_swap(lst: List[int], i: int, j: int):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

# A simple sorting algorithm
def my_sort(lst: List[int]):
    for j in tqdm(range(len(lst))):
        for i in range(len(lst) - j-1):
            if lst[i] > lst[i + 1]:
                list_swap(lst, i, i + 1)

# Like search above, will create a random list and sort it
# using the my_sort function
def sort_test(n: int):
    lst = [random.randint(0, 10 * n) for i in range(n)]
    print('Go!')
    st = datetime.now()
    my_sort(lst)
    print(datetime.now() - st)




# Same, but using the built-in Python sorting algorithm
def sort_test_python(n: int):
    lst = [random.randint(0, 10 * n) for i in range(n)]
    print('Go!')
    st = datetime.now()
    sorted(lst)
    print(datetime.now() - st)


# A *very* inefficient way to sort:

def is_sorted(lst: List[int]) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def permute_sort(n: int):
    lst = [random.randint(0, 10 * n) for i in range(n)]
    print('Go!')
    st = datetime.now()
    for item in itertools.permutations(lst):
        if is_sorted(item):
            print(datetime.now() - st)
            return True



# Sorting using the tree idea
def sort_test_tree(n: int):
    lst = [random.randint(0, 10 * n) for i in range(n)]
    print('Go!')
    st = datetime.now()
    r = bst_list(lst)
    print(f'Tree Built in {datetime.now() - st}')
    sort_time = datetime.now()
    new_lst = sort_tree(r)
    print(f'Total: {datetime.now()-st}  Sort: {datetime.now() - sort_time}')





class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'Node({self.value})'

    def __str__(self):
        numb_child = 0
        if self.left:
            numb_child += 1
        if self.right:
            numb_child += 1
        return f'Node with value {self.value} and {numb_child} children.'


    # this is a long, awkward bit of code that prints a Binary Search tree
    # this is not great code, but I implemented it quickly to be able to show the tree
    def print_bst(self):
        lst = [[self]]

        go = True
        while go:
            temp = []
            for node in lst[-1]:
                if node and node.left:
                    temp.append(node.left)
                else:
                    temp.append(None)
                if node and node.right:
                    temp.append(node.right)
                else:
                    temp.append(None)
            if temp!= [None] * len(temp):
                lst.append(temp)
            else:
                go = False

        curr_height = 0
        max_height = len(lst) - 1
        return_str = ''

        for row in lst:

            for item in row:
                return_str += ' ' * (2 ** (max_height - curr_height + 1)  - 1)
                if item:
                    return_str += str(item.value)
                else:
                    return_str += ' '
                return_str += ' ' * (2 ** (max_height - curr_height + 1) - 1)
                return_str += ' '
            curr_height += 1
            return_str += '\n\n'

        print(return_str)





# this is how we put new nodes into the tree
    def insert(self, value):
        if value < self.value:
           if self.left:
               self.left.insert(value) # notice that this is recursion
           else:
               self.left = Node(value)

        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

# notice something fairly deep here -- a Node knows which children (if any) it has
# Nodes do not know their parents!




#
def sort_tree(root: Node) -> List[int]:
    lst = []

    if root.left:
        lst += sort_tree(root.left)

    lst += [root.value]
    if root.right:
        lst += sort_tree(root.right)

    return lst

def get_min(root: Node) -> int:
    if root.left:
        return get_min(root.left)
    return root.value

def get_max(root: Node) -> int:
    if root.right:
        return get_max(root.right)
    return root.value

def search(root: Node, value: int) -> bool:
    if root.value == value:
        return True
    elif value < root.value and root.left:
        return search(root.left, value)
    elif value > root.value and root.right:
        return search(root.right, value)
    else:
        return False



def bst_list(lst: List[int]):
    root = Node(lst[0])
    for item in lst:
        root.insert(item)

    return root







