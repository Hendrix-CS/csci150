CSCI 150 HW: conditional practice
---------------------------------

*Due: Monday, February 4*

1. Find at least 5 errors in the following code.  For each error,
   explain what is wrong and how you would fix it.

    ```
    fruit = print("What is your favorite fruit?)
    number = int(input("Pick a number between 1 and 10")
    if fruit == "banana":
       print("Yes, we have no bananas.")
    elif fruit == "apple" and number > 4 or < 20
       print("Soo many apppplles.")
    if fruit == "pear":
       elif number > 6:
       print("We need to pear that down a bit.")
       else:
          print("Pearfect!")
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

