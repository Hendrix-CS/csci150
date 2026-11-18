from dataclasses import dataclass

# Reminders
# No quiz on Friday
#
# Project Design Documents Returned through Teams
#

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
    left: 'Node' = None
    right: 'Node' = None