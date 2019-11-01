CSCI 150 HW: dictionary + heap reading practice
-----------------------------------------------

*Due: Wednesday, November 6*

To receive full credit, for each exercise you should do the following:

1. **Predict**: First, complete the exercise *without* using the
   Python interpreter.  *Trace the execution of the code, keeping
   track of the function stack, the heap, all variables, and any
   output produced.*

    If you like, you may print out copies of the tracing template
    found at
    [`http://ozark.hendrix.edu/~yorgey/150/static/heap-tracing-template.pdf`](http://ozark.hendrix.edu/~yorgey/150/static/heap-tracing-template.pdf)
    (if you have this PDF open on your computer you may simply click
    the link above).

2. **Check**: Run the code.  Does the actual output agree with what
   you wrote down in step 1?

3. **Evaluate**: If your answer to part 1 was different than the
   actual output, keep experimenting with it, consult the textbook or
   Python documentation, ask a friend or TA or professor, *etc.* until
   you can explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.

You should consider the code in each exercise separately from the
other exercises.

This line is intentionally left blank.

1. Trace the execution of the following code.

    ``` python
    def alice(lst : List[int], n : int):

        len_lst : int = len(lst)
        for i in range(len_lst):
            lst[i] = lst[i] % n

    def bob(lst: List[int]) -> str:
        s = ''
        letters: List[str] = ['t','e','a','h','p','!','s','y']
        for num in lst:
            s += letters[num]

        return s

    def main():

        mylist = [3,25,14,-2,5]
        alice(mylist,6)
        print(bob(mylist))

    main()
    ```


2. Trace the execution of the following code.

    ``` python
    def harry(s: str)-> Dict[str,int]:
        return_dict = {}
        for char in s:
            return_dict[char] = s.find(char)

        return return_dict

    def hermione(s: str, in_dict: Dict[str,int]):
        for char in s:
            if char in in_dict:
                in_dict[char] += s.find(char)
            else:
                in_dict[char] = -5

    def main1():
        s = '4 privet drive'

        main_dict = harry(s)
        hermione('hendrix',main_dict)
        for key in main_dict:
            print(key + " " + str(main_dict[key]))

    main1()
    ```
