---
layout: work
type: Homework
num: 8
worktitle: For Loop Homework
---



*Due: Monday, October 27 *

Consider the following exercises in CodingBat.  Be
sure to share your progress with me, by going to "prefs" and entering
your instructor's email address (`seme@hendrix.edu` or `yorgey@hendrix.edu') in the "Teacher Share" box.

- [string_splosion](https://codingbat.com/prob/p118366)
- [string_bits](https://codingbat.com/prob/p113152)
- [array_count9](https://codingbat.com/prob/p166170)
- [array123](https://codingbat.com/prob/p193604)
- [string_match](https://codingbat.com/prob/p182414)


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


1. Write, using a `for' loop, a function which given a list of integers, return a count of the number of even integers in the list

2. What is printed by the code below?

 ``` python
    s = 'abcdef'
    v = 'aeiou'
    count = 0
    for char in s:
        if char in v:
            count += 1
    print(count)
 ```

3. What is the value of `new_list` after the code below runs?

 ``` python
    lst = [5, 1, 4, 7, 8, 10, 2]
    new_list = []
    for item in lst:
        if item % 2 == 0:
            new_list.append(item // 2)
        else:
            new_list.append(item)
 ```

