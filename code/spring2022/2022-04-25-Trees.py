from typing import *
from datetime import datetime
import random

# directly below is a new library, which can provide
# a progress bar for loops

from tqdm import tqdm




###########
# Here is our code for building a tree from last time



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
def sort(root: Node) -> List[int]:
    lst = []

    if root.left:
        lst += sort(root.left)

    lst += [root.value]
    if root.right:
        lst += sort(root.right)

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





def time_test(n: int):
    test_list = []
    for k in range(n):
        test_list.append(random.randint(0,n * 5))

    print('Linear Search')
    counter = 0
    st = datetime.now()
    for k in tqdm(range(0,n * 5)):

        if k in test_list:
            counter += 1
    print(datetime.now() - st, counter)

    print('Binary Search')
    st = datetime.now()
    root = Node(test_list[0])
    for item in test_list:
        root.insert(item)

    counter = 0

    for k in tqdm(range(0, n * 5)):

        if search(root,k):
            counter += 1
    print(datetime.now() - st, counter)

# We notice how much more efficient a Tree is

# In more advanced computer science courses, we care a lot about
# whether or not code might be efficient


#############################

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n //2
    else:
        return 3 * n + 1

def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = hailstone(n)
        steps += 1
    return steps




def collatz_dict_builder(n: int) -> Dict[int, int]:
    d = {}
    for i in tqdm(range(1, n + 1)):
        d[i] = collatz_steps(i)

    return d


def collatz_steps2(n: int, d: Dict[int, int]) -> int:
    steps = 0
    while n != 1:
        if n in d:
            return steps + d[n]
        n = hailstone(n)
        steps += 1
    return steps


def collatz_dict_builder_memo(n: int) -> Dict[int, int]:
    d = {}
    for i in tqdm(range(1, n + 1)):
        d[i] = collatz_steps2(i, d)

    return d



def prime_factors(n: int) -> List[int]:
    primes = []
    k = 2
    while k <= n ** (1/2):
        if n % k == 0:
            primes.append(k)
            n = n // k
        else:
            k += 1
    primes.append(n)


    return primes

def prime_dict(n: int) -> Dict[int, List[int]]:
    d = {}
    for i in tqdm(range(2,n+1)):
        d[i] = prime_factors(i)

    return d

def prime_factors2(n: int, d: Dict[int, List[int]]) -> List[int]:
    primes = []
    k = 2
    while k <= n ** (1/2):
        if n in d:
            return primes + d[n]
        if n % k == 0:
            primes.append(k)
            n = n // k
        else:
            k += 1
    primes.append(n)


    return primes

def prime_dict_memo(n: int) -> Dict[int, List[int]]:
    d = {}
    for i in tqdm(range(2,n+1)):
        d[i] = prime_factors2(i, d)

    return d