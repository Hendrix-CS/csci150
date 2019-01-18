# Trees

class Tree:

    # self.value  --- value @ the root
    # self.children: List[Tree]

    def __init__(self, value, children):
        self.value = value
        self.children = children

    # Return the number of items in the whole tree
    def size(self) -> int:

        # Base case is not necessary

        # if len(self.children) == 0:
        #     return 1
        # else:

        total: int = 1
        for child in self.children:
            total += child.size()

        return total

    # Add up all the values in the whole tree
    def sum(self) -> int:
        total: int = self.value
        for child in self.children:
            total += child.sum()
        return total

    # Print the tree in outline form, e.g.
    #
    # cat
    #   horse
    #   leaf
    #     potato
    #   sock

    def print_outline(self):
        self.print_outline_indented(0)

    def print_outline_indented(self, indent: int):
        print((' ' * indent) + str(self.value))
        for child in self.children:
            child.print_outline_indented(indent + 2)


def main():
    t = Tree(3, [Tree(2, []), Tree(5, [Tree(19, []), Tree(22, []), Tree(10, [])])])
    print(t.size())
    print(t.sum())

    t2 = Tree('cat', [Tree('horse', []), Tree('leaf', [Tree('potato', [])]), Tree('sock', [])])
    print(t2.size())
    print(t2.sum())

    t2.print_outline()

main()