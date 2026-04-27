from datetime import datetime

def f(n: int) -> int:
    if n == 0:
        return 2
    else:
        return 3 * f(n - 1)


def g(s: str) -> int:
    if len(s) == 0:
        return 0
    else:
        if s[0] < 'k':
            return 1 + g(s[1:])
        else:
            return g(s[1:])


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_time(max: int):
    n = 0
    while n <= max:
        st = datetime.now()
        print(f'{n};{fib(n)}; {(datetime.now()-st).total_seconds()}')
        n += 1




def memo_fib(n: int, d) -> int:
    d[0] = 1
    d[1] = 1
    if n not in d:
        d[n] = memo_fib(n - 1, d) + memo_fib(n - 2, d)
    return d[n]


def memo_fib_time(max: int):
    n = 0
    while n <= max:
        st = datetime.now()
        print(f'{n};{memo_fib(n, {})}; {(datetime.now()-st).total_seconds()}')
        n += 1
