---
layout: work
type: Homework
num: 6
worktitle: List Homework
---

Complete each of the five excercises in CodingBat
- [count_evens](https://codingbat.com/prob/p189616)
- [centered_average](https://codingbat.com/prob/p126968)
- [sum13](https://codingbat.com/prob/p167025)
- [sum67](https://codingbat.com/prob/p108886)
- [has22](https://codingbat.com/prob/p119308)

For each of the following excercises:

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

Suppose that `lst = [5, 7, 10, 2, 3]`.

Find the vlaue of each expression:

1. `lst[2]`
2. `lst[2:4]`
3. `lst[:3]`
4. `len(lst)`
5. Consider the following code.  What is printed by the final line,
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

6. What is printed by the following code?

    ``` python
    animals = ['caiman', 'bat', 'dingo', 'chihuahua', 'baboon', 'fox', 'galapagos']

    i = 0
    while i < len(animals):
        if (animals[i][1] == 'a'):
            print(animals[i])

        i += 1
    ```


