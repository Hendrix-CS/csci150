def foo(a: int) -> int:
    b = 3*a + 2
    return b
    print("In foo")

def bar(x: int, y: int) -> int:
    return foo(x) + foo(y)

def main1():
    print("The value is " + str(bar(2,3)))

########################################

def f1():
    print("mushroom")

def f2():
    f1()
    print("badger")
    f1()

def f3(n: int):
    f2()
    if n > 5:
        print("snake")
        f1()
    else:
        print("snaaaaake")

def main2():
    f3(2)
    f3(6)

########################################

def main3():
    s: int = 0
    i: int = 0
    while i < 5:
        j: int = 0
        while j < i:
            s += j
            j += 1
        i += 1
    print(s)
