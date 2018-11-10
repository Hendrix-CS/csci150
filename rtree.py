class Tree:
    def __init__(self, val: int, children):
        self.val = val
        self.children = children

    def __repr__(self):
        s = "Tree(" + str(self.val) + ", ["

        children_strs = []
        for c in self.children:
            children_strs.append(str(c))

        s += ', '.join(children_strs)
        s += "])"

        return s

    def sum(self) -> int:
        total: int = 0
        total += self.val
        for c in self.children:
            total += c.sum()

        return total

    def max(self) -> int:
        m: int = self.val
        for c in self.children:
            cm = c.max()
            if cm > m:
                m = cm
        return m

    def size(self) -> int:
        total: int = 1
        for c in self.children:
            total += c.size()

        return total

    def inc(self):
        self.val += 1
        for c in self.children:
            c.inc()

def grow(n: int) -> Tree:
    if n == 0:
        return Tree(0, [])
    else:


def main():
    t = Tree(3, [Tree(2, []), Tree(4, [Tree(1, []), Tree(7, [])]), Tree(19, [])])
    print(t)
    print(t.sum())
    print(t.max())
    print(t.size())
    t.inc()
    print(t)

main()
