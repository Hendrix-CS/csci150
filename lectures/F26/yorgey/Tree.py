# A tree consists of:
#   - some kind of value stored at the "root"
#   - a list of "children", which are themselves trees.

# Real world examples:
#   - org chart / hierarchy
#   - family tree
#   - dialog tree / skill tree
#   - expert system
#   - classification systems (animals, Dewy Decimal system, etc.)
#   - pyramid schemes
#   - chess openings / game tree

from dataclasses import dataclass

@dataclass
class Tree:
    root: str
    children: list[Tree]

    # size = number of values
    def size(self) -> int:
        result = 1
        for child in self.children:
            result += child.size()   # recursively add up all child sizes

        return result

    def display(self) -> str:
        return self.display_indented(0)

    def display_indented(self, indent: int) -> str:
        result = ' '*indent + self.root
        for child in self.children:
            result += "\n" + child.display_indented(indent + 2)

        return result



example_tree = Tree("cat", [Tree("leopard", [Tree("snow leopard", []), Tree("mighty leopard", [])]), Tree("lion", []), Tree("housecat", [])])