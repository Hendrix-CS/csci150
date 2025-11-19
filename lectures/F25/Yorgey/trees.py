# Trees, i.e. hierarchies, show up all over the place!

# A tree has:
#   (1) a value
#   (2) a list of "children", which are themselves trees.

from dataclasses import dataclass

@dataclass
class Tree:
    value: str
    children: list['Tree']

    # Calculate the number of values in a tree
    def size(self) -> int:
        # size of the tree is 1 + sum of the sizes of all its children
        s = 1
        for t in self.children:
            s += t.size()

        return s

    # Concatenate all strings into one long string
    def flatten(self) -> str:
        result = self.value
        for t in self.children:
            result += t.flatten()
        return result

    # Format a tree with one value per line, using indentation to show
    # children
    #
    # e.g.
    #
    # XYZ
    #   Q
    #   A
    #     B
    #     C
    #   P
    def format(self) -> str:
        return '\n'.join(self.format_list())

    def format_list(self) -> list[str]:
        result = [self.value]
        for t in self.children:
            sub_list = t.format_list()
            for line in sub_list:
                result.append('  ' + line)

        return result

example1: Tree = Tree('A', [])
example2: Tree = Tree('A', [Tree('B', []), Tree('C', [])])

#     A
#    / \
#   B   C

example3: Tree = Tree('XYZ', [Tree('Q', []), example2, Tree('P',[])])

#         XYZ
#    /    |   \
#   Q     A    P
#        / \
#       B   C