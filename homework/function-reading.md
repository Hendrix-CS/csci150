HW: function reading practice
-----------------------------

XXX probably should add one more (harder) exercise

You should complete the following exercises *without* using a
computer!

1. Consider the functions defined below.  What does `main()` print?

    ``` python
    def foo(a):
        b = 3*a + 2
        return b
        print "In mystery1"

    def bar(x,y):
        return foo(x) + foo(y)

    def main():
        print "The value is " + str(bar(2,3))
    ```

2. Consider the functions defined below.  What is printed by `main2()`?

    ``` python
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
    ```
