CSCI 150 HW: Python tracing practice
------------------------------------

*Due: Wednesday, September 5*

To receive full credit, for each exercise you should do the following:

1. **Trace**: First, trace the execution of each Python program below,
   using the template shown in class.  That is, scratch work goes in
   the upper left; keep track of the types and values of any variables
   in the upper right; and show any printed output from the program at
   the bottom.  You should complete the exercise *without* using the
   Python interpreter.  (You are welcome to refer to your notes or
   textbook, read Python documentation, look at examples from class,
   *etc.*; just don't actually run any code.)

2. **Check**: Now run the code.  Does the actual output agree with
   what you wrote down in step 1?

3. **Evaluate**: If your answer to part 1 was different than the
   actual output, keep experimenting with it, consult the textbook or
   Python documentation, ask a friend or TA or professor, *etc.* until
   you can explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.  (You do not need to do
   anything for step 3 if the output agrees exactly with what you
   wrote in step 1.)

You should consider the code in each exercise separately from the
other exercises.

1.

    ``` python
    a: float = 3
    b: float = 4
    hyp: float = (a**2 + b**2)**(1/2)
    print("The hypotenuse is " + str(hyp))
    ```

1.

    ``` python
    a1: int = 3
    a2: int = a1 + 9
    a3: int = a1 + a2
    a2 = a1 + a3 - 5
    a1 = a1 + 1
    a3 = a2 * 2 - a1
    a1 = a1 + 1
    print(str(a1) + " -> " + str(a2 + a3))
    ```

2.

    ``` python
    zebra: str = "fish"
    fish: str = "food"
    food: str = "pizza"
    print(fish + " = " + food)
    pizza: str = "zebra" + fish
    print(pizza + "pizza" + zebra + "zebra")
    print(str(5 + 2) + "5 + 2")
    ```

