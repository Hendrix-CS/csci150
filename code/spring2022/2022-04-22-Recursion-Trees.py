from typing import *
from datetime import datetime
import random

# from last time
def is_palindrome(s: str) -> bool:
    if s == '':    # base case
        return True

    else:   # recursive case
        return s[0] == s[-1] and is_palindrome(s[1:-1])













# New Data Structure -- a tree
#
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
#  * File structure on a computer (Enron Lab)
#  * Decision trees
#  * Probability trees
#  * Search Trees -- what we'll actually do today/Monday
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

    def __str__(self):
        numb_child = 0
        if self.left:
            numb_child += 1
        if self.right:
            numb_child += 1
        return f'Node with value {self.value} and {numb_child} children.'


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




