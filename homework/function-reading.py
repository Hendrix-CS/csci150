def foo(a):
    b = 3*a + 2
    return b
    print "In mystery1"

def bar(x,y):
    return foo(x) + foo(y)

def main():
    print "The value is " + str(bar(2,3))

########################################

def f1():
    print "mushroom"

def f2():
    f1()
    print "badger"
    f1()

def f3(n):
    f2()
    if n > 5:
        print "snake"
        f1()
    else:
        print "snaaaaake"

def main2():
    f3(2)
    f3(6)
