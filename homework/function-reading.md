CSCI 150 HW 3: function reading practice
----------------------------------------

You should complete the following exercises *without* using a
computer, though you may consult your textbook.  You should write your
answers by hand and turn them in on paper.

1. Consider the functions defined below.  What does `main()` print?

    ``` python
    def foo(a):
        b = 3*a + 2
        return b

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
