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


2.
    def main2():
      a_dict = {1: 'cat', 2: 'dog', 34: 'fish'}
      b_dict = a_dict
      temp_dict = {}
      for item in a_dict:
        temp_dict[item] = a_dict[item] + '!!'

      b_dict[100] = 'pig'
      a_dict[2] = 'snail'

      print(a_dict)
      print(b_dict)
      print(temp_dict)

    main2()
