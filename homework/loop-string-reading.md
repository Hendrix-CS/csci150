CSCI 150 HW: function, loop, and string reading practice
--------------------------------------------------------------

*Due: Monday, February 26*

To receive full credit, for each exercise you should do the following:

1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.  (You are welcome to refer to your notes or
   textbook, read Python documentation, look at examples from class,
   *etc.*; just don't actually run any code.)  *Trace the execution of
   the code, keeping track of the function stack, all variables, and
   any output produced.*

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

1. Trace the execution of the following code.

    ``` python
    def f(n: int) -> str:
        n = 2 * n + 1
        return str(n)

    def g(n: int):
        s = f(n) + f(n+2)
        print(s)
        print("n is " + str(n))

    def main():
        g(7)
        g(2)

    main()
    ```

    The above code contains one trap for the unwary; what is it?

2. Trace the execution of the following code.

    ``` python
    def q(n: int) -> str:
        s = 'TIPNR'
        return s[n % 5]

    def m():
        i = 2
        count = 0
        s = ''
        while count < 5:
            s += q(i)
            i += 2
            count += 1
        print(s)

    m()
    ```

3. What is printed by the following code?  Hint: read about the `find`
   function
   here: [`https://docs.python.org/3/library/stdtypes.html?highlight=find#str.find`](https://docs.python.org/3/library/stdtypes.html?highlight=find#str.find),
   and try some examples to make sure you understand what it does.

    ``` python
    s = 'thesethickthornythistlethingsthrivethroughoutthethicket'

    pos = 0
    while pos != -1:
        next = s.find('th',pos+1)
        if next != -1:
            print(s[pos:next])
        else:
            print(s[pos:])
        pos = next
    ```
