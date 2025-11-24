from datetime import datetime


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)




def fib_time():
    for k in range(30,42):
        st = datetime.now()
        f = fib(k)
        print(k, f, (datetime.now()-st).total_seconds())

def fib2(n,d):
    d[0] = 1
    d[1] = 1
    if n not in d:
        d[n] = fib2(n-1,d) + fib2(n-2,d)
    return d[n]


def fib_time2():
    for k in range(900,987,5):
        st = datetime.now()
        f = fib2(k,{})
        print(k, f, (datetime.now()-st).total_seconds())



