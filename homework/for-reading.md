CSCI 150 HW: for loop reading practice
--------------------------------------

*Due: Wednesday, October 24*

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

You should consider the code in each exercise separately from the
other exercises.

1. Trace the execution of the following code.

    ``` python
    def aaa(lst: List[int]) -> List[int]:
        bbb: List[int] = []
        for i in range(len(lst)):
            bbb.append(lst[len(lst) - i - 1])

        return bbb

    def main():
        mynums: List[int] = [4,6,2,9]
        print(aaa(mynums))
    ```

3. Trace the execution of the following code.

    ``` python
    xs: List[int] = [0,1,2,3,4]
    for i in range(len(xs)):
        xs[i] = 2*xs[i] + 1

    s: int = 0
    p: int = 1
    for x in xs:
        s += x
        p *= x

    print(s)
    print(p)
    ```

2. Trace the execution of the following code.

    ``` python
    def q(n: int) -> str:
        s: str = 'TIPNR'
        return s[n % 5]

    def m():
        s: str = ''
        for count in range(1,6):
            s += q(2*count)
            i += 2
        print(s)

    m()
    ```

