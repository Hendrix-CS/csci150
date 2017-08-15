CSCI 150 HW: while loop, string, and list reading practice
----------------------------------------------------------

*Due: Monday, February 27*

To receive full credit, for each exercise you should do the following:

1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.  (You are welcome to refer to your notes or
   textbook, read Python documentation, look at examples from class,
   *etc.*; just don't actually run any code.)  Write down what you
   think the output will be.  Most likely you will need to write down
   some intermediate work to keep track of values of variables; feel
   free to include that work as well.

2. **Check**: Run the code.  Does the actual output agree with what
   you wrote down in step 1?

3. **Evaluate**: If your answer to part 1 was different than the
   actual output, keep experimenting with it, consult the textbook or
   Python documentation, ask a friend or TA or professor, *etc.* until
   you can explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.  (You do not need to do
   anything for step 3 if the output agrees exactly with what you
   wrote in step 1.)

You will not be graded on how correct your answer is in part 1.
However, you *will* be graded on the accuracy of your evaluation in
step 3.  Obviously, I will not be able to tell the difference if you
simply run the code and paste the output for step 1; please do not do
that!  You will only be depriving yourself of a learning opportunity
(not to mention that it is a violation of the academic integrity
policy).

Turn in your answers and evaluations either electronically on Moodle,
or on paper.

You should consider the code in each exercise separately from the
other exercises.

1. Consider the following code.  What is printed by the final line,
   `print(mklist(5))`?

    ``` python
    def mklist(n):
        nums = []
        i = 0
        p = 1
        while (i <= n):
            nums.append(p)
            p *= 2
            i += 1
        return nums

    print(mklist(5))
    ```

2. What is printed by the following code?

    ``` python
    animals = ['caiman', 'bat', 'dingo', 'chihuahua', 'baboon', 'fox', 'galapagos']

    i = 0
    while i < len(animals):
        if (animals[i][1] == 'a'):
            print(animals[i])

        i += 1
    ```

3. What is printed by the following code?

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
