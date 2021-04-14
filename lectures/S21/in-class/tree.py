from typing import *
from dataclasses import dataclass

# A Tree represents a hierarchy.  It has one value at the
# top ("root") which has zero or more "children" which are
# themselves trees.

@dataclass
class Tree:
    value: int    # only ints for now
    children: List['Tree']

    def size(self):
        # Notice the for loop already handles the base
        # case (no children)
        total: int = 1     # start with 1 for the root value
        for child in self.children:
            total += child.size()
        return total

tree1: Tree = Tree(3,[])

tree2: Tree = Tree(17, [Tree(6,[]), Tree(5,[Tree(1,[]), Tree(9,[])]), Tree(12,[])])

tree3: Tree = Tree(28, [tree2, tree1])
