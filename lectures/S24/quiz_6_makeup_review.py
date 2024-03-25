def goo(x: int) -> int:
    c = x + 4
    if c > 6:
        return 1
    else:
        return -2

def foo(x: int):
    if x % 3 == 1:
        print(goo(x // 3))
    else:
        print(goo(1 - x) + goo(x + 1))

def main():
    foo(2)
    foo(7)

main()