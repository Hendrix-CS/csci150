class Counter:
    def __init__(self, step: int):
        self.count = 0
        self.step = step

    def inc(self):
        self.count += self.step

    def reset(self):
        self.count = 0

    def get_count(self) -> int:
        return self.count

def incs(c: Counter, n: int):
    for i in range(n):
        c.inc()

def main():
    c = Counter(1)
    d = Counter(2)
    e = c

    incs(c, 3)
    e.reset()
    incs(d, 3)
    incs(e, 4)

    print(f"c: {c.get_count()}, d: {d.get_count()}, e: {e.get_count()}")

main()

from typing import *

class Zipper:
    def __init__(self, words: List[str]):
        self.before = []
        self.after  = words

    def right(self):
        self.before.append(self.after.pop(0))

    def get_cur(self):
        return self.after[0]

    def set_cur(self, new_str: str):
        self.after[0] = new_str

    def unzip(self) -> List[str]:
        return self.before + self.after

def main2():
    z = Zipper(["This", "is", "sorta", "cool"])
    z.right()
    z.right()
    z.set_cur("very")
    print(z.unzip())

main2()
