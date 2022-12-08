CSCI 150 HW: Heap Tracing Practice
---------------------------------------

*Due: Wednesday, April 5*

**Grading Specifications**

You will earn a **Complete** provided that:
- all five problems are attempted,
- at least three are completely correct, showing all changes in the stack and heap as appropriate
- a fourth has minor computational/careless error, but shows correct interactions with the heap, and
- on all five, there is no confusion about print vs return values.

You will earn a **Partially Complete** provided that:
- at least four are attempted
- on at least three, interactions with the heap are correct, except for minor computational errors, and
- there is no confusion on at least two about print vs return values

You are *STRONGLY* encouraged to copy the code shown into a .py file or Kaggle notebook and run them. See if you printed output matches. Add additional print statements along the way to see if you are updating the heap/stack variables correctly. If you are confused, seek help from classmates, the CSCI tutors, or your instructor. If you do so, you might consider adding

`from typing import *`

as the first line of your code.

You should consider the code in each exercise separately from the
other exercises.

1.
    ``` 

    def main1():
      a_list = [1, 2, 3]
      b_list = a_list
      temp_list = []
      for item in a_list:
        temp_list.append(item * 2)

        b_list.append(47)
        a_list[1] = -7

        print(a_list)
        print(b_list)
        print(temp_list)

    main1()
    ```

2. Consider the functions defined below.  What is printed by `main2()`?

    ``` python
    def bbb(d: Dict[str, str]) -> Dict[str, List[str]]:
        mystery = {}
        for word in d:
            if d[word] not in mystery:
                mystery[d[word]] = []
            mystery[d[word]].append(word)
        return mystery

    def main2():
        wordmap = {'hi':'there', 'whoa':'there'}
        wordmap['whoa'] = 'nelly'
        wordmap['you']  = 'there'
        print(bbb(wordmap))
    ```

3. Consider the functions defined below.  What is printed by `main3()`?

    ``` python
    def f(nums: List[int]) -> List[int]:
        nums[1] += 5
        nums = [6,7]
        nums[0] *= 2
        return nums

    def g(ns: List[int]):
        print(ns)
        f(ns)
        print(ns)

    def main3():
        mylist = [6,1,5,2]
        g([3] + mylist)
        print(mylist[0])
    ```
