from typing import *

def oogie(m: List[int]) -> int:
    p = m[0]
    for g in m:
        if g > p:
            p = g
    return p

def yayaya(q: List[str]) -> bool:
    for y in range(len(q) - 1):
        if q[y] == q[y + 1]:
            return True
    return False

def pulu(r: int) -> List[int]:
    b = []
    for k in range(r):
        b.append(k ** 3)
    return b
