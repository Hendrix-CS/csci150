from dataclasses import dataclass


# New Homework - Recursion

# We can write powers recursively:
#
# 3 ** 5 = 3 * (3 ** 4), for example
#
# What is the base case?
#
# The recursive case?





# We could modify this to work for negative integer exponents as well




# Fibonacci
# The Fibonacci Sequence is 1, 1, 2, 3, 5, 8, 13, etc
# We find the next number by adding the previous 2





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

@dataclass
class Node:
    value: int
    left: 'node' = None
    right: 'node' = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)  # notice that this is recursion
            else:
                self.left = Node(value)

        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)


    def print_bst(self): # this is *VERY OVERLY* complicated
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




# Now we can build an use a tree
def make_tree():
    lst = [5, 7, 2, 4, 10, 11, 1, 3,12, 19, 0, 6]
    root = Node(lst[0])
    for item in lst[1:]:
        root.insert(item)

    return root


# Then, we can operate on a binary search tree -- these could be methods in a Tree class if I had more time
def sort(root: Node) -> list[int]:
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