def add_one(n: int) -> int:
    return n + 1


def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def inc_or_double(n: int) -> int:
    if is_even(n):
        return add_one(n)
    else:
        return n * 2


def multiply(a: int, b: int) -> int:
    count = 0
    product = 0
    while count < b:
        product = product + a
        count = count + 1
    return product


def main():
    p = multiply(2, 3)
    if is_even(p):
        print(f"{p} is even")
    else:
        print(f"{p} is odd")

    q = add_one(p)
    if is_even(q):
        print(f"{q} is even")
    else:
        print(f"{q} is odd")

    print(inc_or_double(p))
    print(inc_or_double(q))


main()