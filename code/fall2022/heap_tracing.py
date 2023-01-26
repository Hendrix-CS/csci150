from typing import *


def f1(s: str) -> int:
    if len(s) % 2 == 0:
        return 0
    else:
        return len(s)


def f2(d: Dict[str, int]):
    for key in d:
        d[key] = f1(key)


def main1():
    a = {'alice': 5, 'bob': 9, 'star': -6, '': 7}
    b = a

    c = {}
    for key in b:
        c[key] = b[key]

    f2(b)

    print(a)
    print(b)
    print(c)


main1()
