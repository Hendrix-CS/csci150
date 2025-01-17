---
layout: work
type: Homework
num: 13
worktitle: Recursion
---

To receive full credit, for each exercise you should do the following:

1. **Design**: First, write a Python function as requested in the
   exercise.

2. **Check**: Run the provided test code.  Does your actual output
   agree with the given correct output?

3. **Evaluate**: If the actual output does not match the expected
   output, keep experimenting, consult the textbook or Python
   documentation, ask a friend or TA or professor, *etc.* until you
   can fix your class definition and explain what your
   misunderstanding(s) were.  (You do not need to do anything for step
   3 if the outputs already agree exactly.)

You should consider the code in each exercise separately from the
other exercises.

1. Consider the function `logarithm(b,n)` given below, which counts how many 
  times `n` has to be divided by `b` before falling below `b`:

    ``` python
    def logarithm(b: float, n: float) -> int:
        count = 0
        while n >= b:
            count += 1
            n /= b
        return count
    ```

    Write a new version of `logarithm` which uses recursion instead of
    a `while` loop.

    To test your function, you can type in the following tests:

    ``` python
    def main():
        print(logarithm(2, 128) == 7)
        print(logarithm(2, 35)  == 5)
        print(logarithm(5, 125) == 3)
        print(logarithm(2, 1)   == 0)
        print(logarithm(2, 3)   == 1)
        print(logarithm(10, 19740983) == 7)
    ```

    If you have implemented `logarithm` correctly, `main()` should
    print `True` six times.

2. Write a recursive function `is_palindrome` which takes a string as
   a parameter and returns a `boolean` indicating whether the string
   is a palindrome (a palindrome is a string which is equal to its
   reversal).

    You can test your function with this `main2()`, which should print
    all `True`:

    ``` python
    def main2():
        print(is_palindrome('kayak'))
        print(is_palindrome('kayyak'))
        print(is_palindrome(''))
        print(is_palindrome('a'))
        print(is_palindrome('aa'))
        print(not is_palindrome('ab'))
        print(not is_palindrome('bbbbbbcbbb'))
        print(not is_palindrome('myhelicopterisfullofeels'))
        print(is_palindrome('amanaplanacanalpanama'))
    ```
