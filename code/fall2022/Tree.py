from typing import *

class Tree:

    # self.value  will store the value at the "root"
    # self.children will be a list of children (trees).  (stops when the list is empty).

    def __init__(self, value, children):
        self.value = value
        self.children: List[Tree] = children

    # How many total nodes are in the tree?
    def size(self) -> int:
        total = 1  # counts root node
        for child in self.children:
            total += child.size()
        return total

    # Get a list of the values at a certain
    # generation, i.e. root = gen 0, children = gen 1,
    # grandchildren = gen 2, etc.
    def generation(self, g: int) -> List:
        # Base case:
        if g == 0:
            return [self.value]
        else:
            # Otherwise, ask our children
            # for generation g-1.
            genlist = []
            for child in self.children:
                genlist += child.generation(g-1)
            return genlist

    # Return the maximum number of generations present anywhere in the tree.
    def depth(self):
        if self.children == []:
            return 0
        else:
            max_depth = 0
            for child in self.children:
                max_depth = max(max_depth, child.depth())
            return max_depth + 1

def main():
    example_tree = \
        Tree(5, [
            Tree(7, [
                Tree(14, []),
                Tree(6, [])
            ]),
            Tree(8, [
                Tree(7, [Tree(1,[])])
            ]),
            Tree(12, [])
        ])
    print(example_tree.size())

    print(example_tree.generation(2))

    print(example_tree.depth())

main()