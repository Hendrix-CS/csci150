CSCI 150 HW solutions: conditional practice
-------------------------------------------

1. Find at least 5 errors in the following code.  For each error,
   explain what is wrong and how you would fix it.

    ```
    # Missing end quote mark; add a " after the ?
    fruit = print("What is your favorite fruit?)

    # Missing close paren; put another ) at the end
    number = int(input("Pick a number between 1 and 10")
    if fruit == "banana":
       print("Yes, we have no bananas.")

    # or < 20 is a syntax error; could say  number > 4 or number < 20
    elif fruit == "apple" and number > 4 or < 20
       print("Soo many apppplles.")
    if fruit == "pear":

       # elif can't be by itself; change 'elif' to 'if.
       elif number > 6:

       # Need to indent this line.
       print("We need to pear that down a bit.")
       else:
          print("Pearfect!")

    # else can't have a condition; either remove condition or change
    #   'else' to 'elif'.
    else fruit == "blackberry":
       print("My favorite!")
    ```

For each of the following scenarios, write some Python code to
generate the intended output.

2. Assume there is a variable `s` which contains a string. If the
   string comes before `f` in the dictionary, print `Fizz`.  If the string
   is after `b` in the dictionary, print `Buzz`. If both the `f` and
   `b` conditions are true, print `FizzBuzz`. In all other cases,
   print the string `s` unchanged.

    ```{.python}
    if 'b' < s < 'f':      # Need to put the most specific condition first!
        print("FizzBuzz")
    elif s < 'f':
        print("Fizz")
    elif 'b' < s:
        print("Buzz")
    else:
        print(s)
    ```

3. We are having a party with amounts of tea and candy; assume there
   are variables named `tea` and `candy` which contain integers. Print
   the outcome of the party: either `bad`, `good`, or `great`. A party
   is good if both tea and candy are at least 5. However, if either
   tea or candy is at least double the amount of the other one, the
   party is not just good but great. In all cases, if either tea or
   candy is less than 5, the party is always bad.

    For example,

    * If `tea == 3` and `candy == 7`, you should print `bad`
    * If `tea == 6` and `candy == 5`, you should print `good`
    * If `tea == 6` and `candy == 12`, you should print `great`

    ```{.python}
    if tea < 5 or candy < 5:
        print("bad")
    elif tea >= 2*candy or candy >= 2*tea:
        print("great")
    else:
        print("good")
    ```
