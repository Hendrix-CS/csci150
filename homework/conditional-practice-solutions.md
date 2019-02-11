CSCI 150 HW solutions: conditional practice
-------------------------------------------

1. Find at least 5 errors in the following code.  For each error,
   explain what is wrong and how you would fix it.

    ```
    # Missing end quote mark; add a " after the ?
    # Also, print does not return a value so assigning fruit = print(...)
    #   does not make sense.  Probably it should say input instead of print.
    fruit = print("What is your favorite fruit?)

    # Missing close paren; put another ) at the end
    number = int(input("Pick a number between 1 and 10")
    if fruit == "banana":
       print("Yes, we have no bananas.")

    # or < 20 is a syntax error; could say  number > 4 or number < 20
    # Also, number > 4 or number < 20 is always true; it is not a syntax
    #   or runtime error but it probably represents a semantic error
    #   (why bother writing a condition that is always true?).
    #   Probably the 'or' should be replaced with 'and'.
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

    Some notes:

    * Be sure to put quotes around `'b'` and `'f'` (since we are
      referring to literal strings) but *not* around `s` (since we are
      referring to the value contained in the variable `s`).
    * The condition for `'b' < s < 'f'` needs to come first.
      Otherwise one of the other conditions will be chosen first and
      Python will never even consider this case.
    * It should not be necessary to use the `str(...)` conversion
      function, which is only needed to convert something which
      *isn't* already a string into a string.
    * Note that the way the problem is stated, you are already given
      a variable `s` which contains a string.  It is not necessary to
      write your own `input` statement. (If it were, the problem would
      say something like "Prompt the user for...")

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

    One solution (not the only correct solution!):

    ```{.python}
    if tea < 5 or candy < 5:
        print("bad")
    elif tea >= 2*candy or candy >= 2*tea:
        print("great")
    else:
        print("good")
    ```

    Some notes:

    * Again, writing `input` statements is not necessary.
    * `tea` and `candy` are already `int` variables; converting them
      with e.g. `int(tea)` does nothing and is unnecessary.
    * Be sure to use `>=` in the condition `tea >= 2*candy` instead of `==`.
    * Don't have multiple `if` statements; Python will execute each of
      them.  Should have a single `if...elif...else`.
    * In English we tend to state general conditions first and then
      exceptions later, but Python will pick the first condition that
      is true without considering later exceptions.  So the most
      specific/absolute condition needs to go first.  For example,
      this is wrong:

        ```{.python}
        if tea >= 2*candy or candy >= 2*tea:
            print("great")
        elif tea >= 5 and candy >= 5:
            print("good")
        else:
            print("bad")
        ```

    because of a case like `tea = 3, candy = 8`: since `tea < 5`, the
    party should definitely be `"bad"`; however, the above code first
    considers the condition `candy >= 2*tea` which is true, so it will
    print `"great"` instead.
