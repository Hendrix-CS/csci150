from typing import *

def foo2(d: Dict[str, float], n: float):
    d2 = {}
    for k in d:
        if d[k] > 5:
            d2[k] = d[k] - n
    d = d2

def main():
    d = {'p': 7, 'q': 2, 'r': 5.5}
    foo2(d, 3)
    print(d)

main()