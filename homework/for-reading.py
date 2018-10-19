from typing import *

def aaa(lst: List[int]) -> List[int]:
    bbb: List[int] = []
    for i in range(len(lst)):
        bbb.append(lst[len(lst) - i - 1])

    return bbb

def main():
    mynums: List[int] = [4,6,2,9]
    print(aaa(mynums))


xs: List[int] = [0,1,2,3,4]
for i in range(len(xs)):
    xs[i] = 2*xs[i] + 1

s: int = 0
p: int = 1
for x in xs:
    s += x
    p *= x

print(s)
print(p)


def q(n: int) -> str:
    s: str = 'TIPNR'
    return s[n % 5]

def m():
    s: str = ''
    for count in range(1,6):
        s += q(2*count)
    print(s)

m()
