1. Consider the following code.  What is printed by the final line,
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

2. What is printed by the following code?

    ``` python
    animals = ['caiman', 'bat', 'dingo', 'chihuahua', 'baboon', 'fox', 'galapagos']

    i = 0
    while i < len(animals):
        if (animals[i][1] == 'a'):
            print(animals[i])

        i += 1
    ```

