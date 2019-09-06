CSCI 150 HW: conditional practice
---------------------------------

*Due: Wednesday, September 11*

To receive full credit, for each exercise you should do the following:

1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.  *Trace the execution of the code, keeping
   track of the function stack, all variables, and any output
   produced.*

2. **Check**: Run the code.  Does the actual output agree with what
   you wrote down in step 1?

3. **Evaluate**: If your answer to part 1 was different than the
   actual output, keep experimenting with it, consult the textbook or
   Python documentation, ask a friend or TA or professor, *etc.* until
   you can explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.

* For each expression, decide whether it will evaluate to `True` or
  `False`.

    * `False and (True or False)`
    * `(True and (not (False or False)) and (False or (True or False))`
    * `3 ** 2 + 4 **2 == 5 ** 2`
    * `50 < 99 / 3`
    * `"egg" < "excellent"`
    * `"arm" < "aardvark"`
    * `False != (True != (False != (False != True)))`

* Pick two strings `before` and `after` such that `before < your_name < after`.
  For example, someone named `"Grace"` could pick `before = "Fuzzy"` and
  `after = "Grape"` since `"Fuzzy" < "Grace" < "Grape"`.
