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

Upload your code to the class Team page as instructed. For each problem, in addition to the code itself, you should have one or more lines of comments which describe what happened, following the 3 steps below:

1. **Design**: FFirst, write a function or design a Python class as requested in the
  exercise.

2. **Check**: Run the your code against the examples provided.  Does the actual
   output agree with the given correct output?

3. **Evaluate**: If your answer in step 1 was different than the
   actual output, keep experimenting with it, consult an online
   reference, ask a friend or TA or professor, *etc.* until you can
   explain why the code works the way it does *and* what your
   misunderstanding(s) were in part 1.




1. Write a function `vowel_count` which takes in a list of strings (all lower case) and returns a dictionary, keyed on the five vowels a, e, i, o, and u. The value for each should be the total number of entries in the list which contain at least a single copy of that vowel. For example,

`vowel_count(['time', 'is', 'the', 'end'])` returns  `{'a': 0, 'e': 3, 'i': 2, 'o': 0, 'u': 0}`


`vowel_count(['aardvark', 'facetious', 'too', 'to', 'two'])` returns `{'a': 2, 'e': 1, 'i': 1, 'o': 4, 'u': 1}`

(note that we are not counting the total number of a's, or e's,
but how many individual entries in the list contain at least one a)
