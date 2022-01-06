CSCI 150 HW: function and loop reading practice
-----------------------------------------------

*Due: Friday, February 25*

To receive full credit, for each exercise you should do the following:

1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.  (You are welcome to refer to your notes or
   textbook, read Python documentation, look at examples from class,
   *etc.*; just don't actually run any code.)  Trace the execution of
   the code in the exercise, including updating variables and any printed output.

2. **Check**: Run the code.  Does the actual output agree with what
   you wrote down in step 1?

3. **Evaluate**: If your answer to part 1 was different than the
   actual output, keep experimenting with it, consult the textbook or
   Python documentation, ask a friend or TA or professor, *etc.* until
   you can explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.  (You do not need to do
   anything for step 3 if the output agrees exactly with what you
   wrote in step 1.)

You should consider the code in each exercise separately from the
other exercises.

1. Consider the functions defined below.  Trace the execution when
   `main1()` is called.

    ``` python
    def foo(a: int) -> int:
        b = 3*a + 2
        return b
        print("In foo")

    def bar(x: int, y: int) -> int:
        return foo(x) + foo(y)

    def main1():
        print(f"The value is {bar(2,3)}")

    main1()
    ```

2. Consider the functions defined below.  Trace the execution when
   `main2()` is called.

    ``` python
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

    main2()
    ```

3. Trace the execution when `main3` is called.

    ``` python
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

    main3()
    ```

Your solution should be hand-written (or typed) and contain the following:

- For each piece of code, you should turn in a completed trace, including any printed output, which was generated prior to running the code on a machine.
- If your check in step 2 indicated a mistake, correct it, and explain what you got wrong initially and why the code produces the answer it does.

## Specifications

- To be considered **complete** you must work each given problem, and you must have the correct answer (after step 2 if needed), along with correct explanations where appropriate.
- An assignment will be considered **partial** provided each problem has been attempted and after step 2 all printed output is correct.
