CSCI 150 HW: Heap Tracing Practice
---------------------------------------

*Due: Wednesday, April 12*

**Grading Specifications**

You will earn a **Complete** provided that:
- all five problems are attempted,
- aFour of the five are completely correct; the fifth has a minor, non-obvious error not easily detectible through simple testing, and
- on all five, there is no confusion about print vs return values.

You will earn a **Partially Complete** provided that:
- at least four are attempted,
- at least two are completely correct,
- at least one class problem has a corerctly implemented `__init()__` method, and
- there is no confusion about print vs return values

Upload your
1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.

2. **Check**: Run the your code against the examples provided.  Does the actual
   output agree with what you wrote down in step 1?

3. **Evaluate**: If your answer in step 1 was different than the
   actual output, keep experimenting with it, consult an online
   reference, ask a friend or TA or professor, *etc.* until you can
   explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.

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

3.

    def main3():
      a_str = 'bye'
      b_str = a_str
      temp_str = ''
      for item in a_str:
        temp_str += item + '!'

      b_str += 'z'


      print(a_str)
      print(b_str)
      print(temp_str)

    main3()


4.

    def f1(a: Dict[str, int]) -> int:
      sum1 = 0
      for key in a:
        if a[key] >= 0:
            sum1 += a[key]
        else:
            a[key] = 0

      return sum1

    def main4():
      b = {'Seme' : 23, 'Ferrer' : 12, 'Wilson' : -7}
      print(f1(b))
      print(b)

    main4()


5.

    def g1(s: str) -> int:
      if 'a' in s:
        s = 'boo'

      return len(s)

    def g2(lst: List[int]):
      s = 'exam'

      if len(lst) < len(s):
        print('Too short')
      else:
        i = 0
        for char in s:
          lst[i] = g1(char)
          i += 1


    def main5():
      a_list = [6,2,9,8]
      g2(a_list)
      print(a_list)

    main5()
