---
layout: work
type: Homework
num: 2
worktitle: Booleans and Conditionals
---

*Due: Monday, September 15*

Remember that homework is not formally assessed. However, any problems turned in by the due date will be checked and feedback provided.

If you need to redo the associate quiz module, before you retake the quiz, you must have the homework completed and checked by your instructor.

1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.

2. **Check**: Run the code in a Kaggle notebook.  Does the actual
   output agree with what you wrote down in step 1?

3. **Evaluate**: If your answer in step 1 was different than the
   actual output, keep experimenting with it, consult an online
   reference, ask a friend or TA or professor, *etc.* until you can
   explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.

For each expression, decide whether it will evaluate to `True` or
`False`.

1. `False and (True or False)`
2. `(True and (not (False or False))) and (False or (True or False))`
3. `3 ** 2 + 4 ** 2 == 5 ** 2`
4. `50 < 99 / 3`
5. `((1 < 2) and ("hi" > "there")) or (99 != 9)`
6. `"egg" < "excellent"`
7. `"arm" < "aardvark"`
8. `False != (True != (False != (False != True)))`

    For problems 9-12, assume that the following variable assignments have been made:
    ```
    x = 7
    y = 2
    ```

9. `x < y`
10. `x + y == (y + 1) ** y`
11. `not( x < y )`
12. `(2 < y) or (3 < x)`


13. What is the value of `a` after the following lines have run:

    ```python
    a = 3
    b = a
    b = b + 2
    ```

14. What is printed by the following code:

    ```python
    s = 'hi'
    t = 'hello'
    if s < t:
       print(t)
    elif s == t:
       print('same!')
    else:
       print(s)
    ```

15. What is the value of `x` after the following lines are run:

    ```python
    x = 5
    if x < 6:
       x = x + 10
    elif x > 9:
       x = 100
    else:
       x = 20
    ```

Your solution should be hand-written (or typed) and contain the following:

- For each line of code above, write down your *original* prediction.
- If your check (step 2) matched, put a check mark. Otherwise, put an X.
- If you wrote an X, then write a brief sentence explaining what you got wrong initially and why the code produces the answer it does.

**Note.** While many of the above can be done quickly "in your head," it can be useful to write out intermediate steps. This is not *required*, but is great practice.

<!--
- An assignment will be considered **partial** if there are no more than 2 wrong answers (after step 2) and no more than two explanations that are given are incorrect.
-->


<!---As usual for this semester, you should submit your work as a PDF,
either by creating it on a computer in the first place or by scanning it.-->
