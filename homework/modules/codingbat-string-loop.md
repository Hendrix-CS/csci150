---
layout: work
type: Homework
num: 5
worktitle: CodingBat String and Loop Practice
---

Consider the following exercises in CodingBat.

- [make_abba](https://codingbat.com/prob/p182144)
- [a_to_e](https://codingbat.com/prob/p269089)
- [make_out_word](https://codingbat.com/prob/p129981)
- [num_vowels](https://codingbat.com/prob/p266191)
- [without_end](https://codingbat.com/prob/p138533)
- [combo_string](https://codingbat.com/prob/p194053)
- [left_2](https://codingbat.com/prob/p160545)


## Specifications

To be considered **complete** you must finish at least five CodingBat exercises *and* complete the excercises below:



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

1. What is printed by the following code?

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

2. What is printed by the following code?

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
