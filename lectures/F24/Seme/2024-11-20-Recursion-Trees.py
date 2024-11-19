from typing import *
from datetime import datetime
import random




# There are lots of recursive ideas in mathematics and computer science, beyond "simple" arithmetical operations

# Ex: When is a word a palindrome?
# When the first and last characters agree and the middle is also a palindrome

# Fractal Images
#

# Trees (real and as a formal idea)

# Search -- maze solutions,

# Many repetitive processes can be thought of recursively

# File structure on a computer -- Folders, which contain folders, which contain ...


# The following is a *BAD* useage of recursion
# Please *DO NOT DO THIS *******
def y_n_bad() -> bool:
    ans = input('Enter yes or no. ')
    if ans == 'yes':
        return True
    elif ans == 'no':
        return False
    else:
        y_n_bad()




## New for today

# Data Structure -- a way to organize information
# * Integers (and floats) -- hold a single value, but the basic numerical data structure
# * Lists -- the basic linear, sequential data structure
# * Strings -- like lists, but specifically about characters
# * Dictionaries -- like lists, but not really linear (there is not really a "next" key)
# * Classes -- a choose-your-own adventure type
# (Others we have not talked about: Hash Tables, Linked Lists, Graphs, ...
#  these are covered in CSCI 151)

# Speaking **very** loosely:
# * Integers are the basic single-value data structure -- they just "are"
# * Lists are the basic linear data structure -- loop over with for loop
# * Trees (new today) are the basic recursive data structure -- hold information and used recursively



# A tree is a data structure where each entry is a "node". Each node has a value
# and each node may or may not have "children"
# One node is identified as the "root"
#
#
#                    Root
#                    /  \
#                 Node    Node
#               /    |        \
#            Node    Node      Node
#           /         /
#          Node    Node
#         /
#        Node

# Trees are used throughout mathematics and computer science:
#  * File structure on a computer
#  * Decision trees
#  * Probability trees
#  * Search Trees -- what we'll actually do today/Friday
#  * Network communications
#  * Many, many more

# In each case, we are organizing some data in a structured way

# We are going to build a binary search tree (BST) --
# * Makes for efficient look up -- is "x" an element of the tree?
# * Makes for efficient sorting -- return all of the elements of the tree in order by value

# A binary tree is one in which each node has at most two children,
#  typically referred to as "left" and "right".


# Unlike lists, or dictionaries, we have to build the tree structure ourselves:



class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'Node({self.value})'

    # def __str__(self):
    #     numb_child = 0
    #     if self.left:
    #         numb_child += 1
    #     if self.right:
    #         numb_child += 1
    #     return f'Node with value {self.value} and {numb_child} children.'


    def print_bst(self): # this is  beyond what I'd expect you to do
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


def make_tree():
    lst = [5, 7, 2, 4, 10, 11, 1, 3,12, 19, 0, 6]
    root = Node(lst[0])
    for item in lst[1:]:
        root.insert(item)

    return root

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
    for k in range(0,n * 5):

        if k in test_list:
            counter += 1
    print(datetime.now() - st, counter)

    print('Binary Search')
    st = datetime.now()
    root = Node(test_list[0])
    for item in test_list:
        root.insert(item)

    counter = 0

    for k in range(0, n * 5):

        if search(root,k):
            counter += 1
    print(datetime.now() - st, counter)




