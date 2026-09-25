#1
def f(n: int):
    i = 0
    while i < n:
        print(i)
        i += 1   # i = i + 1

def main1():
    f(2)
    f(4)

main1()



############
# 2

def g1(n: int) -> int:
    if n > 3:
        return n + 1
    else:
        return n - 3

def g2(n: int):
    i = 2
    while i < n:
        print(g1(i))
        i += 1

def main2():
    g2(1)
    g2(4)
    g2(5)

#main2()


########################
# 3

def h(a: int, b: int):
    count = 0
    while a < b:
        i = 0
        while i < a:
            count += i
            i += 1

        a *= 2

    return count

def main3():
    x = h(2,7)
    print(x)

#main3()