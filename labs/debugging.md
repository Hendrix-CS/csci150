---
layout: work
---
# Lab 13: On Stuckness and Debugging

## Overview

As you certainly know by now, finding and fixing errors is an integral part
of programming. If anything, this becomes more so, not less, the more
experienced of a programmer you become (although the types of errors you
  have to fix may get more sophisticated).

It is thus worthwhile to practice and reflect on the process of debugging
itself. Debugging is, in a very real sense, **an application of the
scientific method**: one makes observations, collects data, comes up with
hypotheses, designs experiments to test the hypotheses, and so on. But, as
we will see, as with any science, debugging is not **only** an application
of the scientific method. In addition to objective analysis, it also often
requires intuitive insights which you can develop, over time, by conscious
application. This lab will give you some directed practice in finding and
fixing programming errors, and help you reflect on the practice of debugging.

Incidentally, if you are wondering why errors in a computer program are
called "bugs", it is not necessarily clear, since the term had been in use
in engineering even before the advent of computers. However, there is a famous
instance of a computer bug discovered by
[Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), one of the
early pioneers of computing.

![Hopper Bug](../assets/images/Hopper-bug.jpg)

This is a page from Hopper's notebook, where she taped a moth found in a
relay switch along with the note "First actual case of bug being found."
Just be glad that you no longer have to be worried about actual bugs
being the source of errors in your programs...

*Acknowledgements: Portions of this lab, including the text for steps
1 and 4 below were adapted from a lab assignment in CS 170 at Emory University.*

## Materials

* Lab Partner(s): for this lab you are **required** to
work in groups of **two or three**.
* [`sum-practice.py`](../code/sum-practice.py)
* [`guess.py`](../code/guess.py)

## Description

### Step 1: Sum practice

The code above contains several errors. Specifically, it contains several
syntax errors, a runtime error, and a semantic error. Your task for this
step is to find and correct these errors.

For each fix, you should add a comment to the file explaining what was wrong
and how you fixed it. For example, if the file contained

    ...
    x = random.random(
    ...

you should change it to something like the following:

    ...
    # Fixed syntax error: added missing closing )
    x = random.random()
    ...

First, try to run the program and look at the generated error(s). Fix the
syntax errors in the file by looking at the line numbers in your program that
Python specifies. (Hint: the error message is not always exactly right about
  the cause of the error! Try looking above the place where Python says
  there is an error.)

After you fix the syntax errors in the program, you will see a runtime error.
Carefully read the error message and look at the code. Try to identify the
problem in the code. Remember that small details such as capitalization and
punctuation matter a great deal. If you can't identify the source of the
runtime error, ask your instructor or TA for help. Remember to add a comment
explaining the problem and solution.

After you fix the runtime error, try running the program again. Success! ...or
is it? The program SHOULD compute the sum of the first n odd integers. Does
the program give you the correct answer? Double check, since you should NEVER
assume the program is giving you the correct answer just because it runs.
Indeed, you should know what answer you expect the program to compute before
you run it. Otherwise, how will you know if your program is correct?

Try running the program with different inputs. If you notice a pattern, this
will give you a clue to the semantic error.

Collecting data is often a key part of gaining the insight necessary to
diagnose an error. One good way to collect data is to instrument a program
to generate information about intermediate results. In particular, let's add
a statement to print out intermediate results, every time the loop executes.
Add the statement

    print("Adding " + str(odd) + " to the current sum " + str(sum))

as the first line of code inside the while loop.

Run your program again. The statement you added now prints out some very
useful information. Printing out intermediate results inside of a loop can
be a good strategy for finding semantic errors in your code. You can add
more print statements if you think other information would be useful.

Finally, fix the program so it correctly computes the sum of the first N
odd numbers, as advertised.

### Step 2: Stuckness

Now that you are warmed up, let's step back and think about the
process of finding and fixing errors itself.  Read
this excerpt from
[Zen and the Art of Motorcycle Maintenance](../homework/zen2.html).
Then, together with your partner(s), answer the following
questions and write your answers in your Evaluation Document.

* What does the narrator mean by "stuckness"?
* Can you identify with the author's description?  In what ways
  is the narrator's description of trying to fix a motorcycle
  similar and different to your experiences in this class?
* What does the narrator say about the relationship between the
  traditional scientific method and being stuck?
* Why does the narrator say that stuckness should not be
  avoided?
* What do you think the narrator means by "Quality"? (I am just
  curious to know what you think; in some sense the entire book is
  about exactly this question, so I certainly don't expect you to
  come up with a complete answer!)
* Did you learn anything from this reading?  Are there ways in
  which you will approach programming and debugging differently as a
  result? ("No" is an acceptable answer, but you should justify
  it!)

### Step 3: Guess the number

The above program emulates a guessing game. Here's a description of how
the game is SUPPOSED to work:

>The game plays five rounds. During each round, the computer picks a random
number between 1 and 6 inclusive. (You can think of this as rolling a 6 sided
die.) The user is then given three chances to guess the chosen number. If the
user guesses correctly, then they win a point, otherwise the computer wins a
point. At the end of five rounds, whoever has the most points wins the game.

However, the program has bugs, and it doesn't follow the rules currently. (As
an aside, this exercise is a great example of why you should never write a lot
of code before you test and debug. It's much harder to debug this program now t
hat it's "finished" then it would be if you practiced incremental development
and fixed the errors as you went along!) Your job is to make the program
follow the above rules by finding and correcting semantic errors.

Before looking at the code, run the program to see what it does. When debugging
a program, it is vital to collect evidence before making changes to the code.
This helps you build a mental model of how the code works and gives you a
starting point to look for errors. Sometimes, you can identify errors without
much effort by carefully tracing the code with the input sequence that causes
an error.

An important aside: because the code generates a different number each time
(what fun would it be to play a game that picked the same number every time?),
it's hard to debug. To make the program's behavior repeatable, we can use
something called a seed, which starts the random number generator in a certain
state. Beginning from the same seed, the same sequence of random numbers will
be generated every time. (If no seed is specified, the current time is used as
a seed, which is why random numbers are usually different every time you run
a program.) To make the code's behavior repeatable, add the line

    random.seed(11)

right after import random. (There is nothing special about the number 11; you
can use any number you want. The important point is that your program will now
use the same seed every time it is run.) Be sure to remove this line before
submitting your final corrected program; otherwise the game will be no fun!

After you have identified one (or more) incorrect behaviors, take a look at
`guess.py`. You should put in print statements like we did above to help you
identify issues as you begin to try to fix the code. It is often useful to
identify a loop or if statement that isn't working the way you think it should,
and print out the variables in its condition immediately before the loop/if
statement executes (or doesn't execute). This gives you an idea of exactly why
your loop/if statement is executing or not. You can then alter the variable to
make the behavior correct. After making a correction or adding more print
statements, run the program again and observe the behavior. Remember to add a
comment explaining each error that you fix!

Did you fix it? If yes, are there other problems? When debugging it is important
to focus on one problem at a time. Once you are satisfied you've corrected that
problem, then run the program again to identify the next problem.

Continue in this way until you are satisfied that the program plays by the rules.

You should be able to identify at least 3 semantic errors. You may have to add
more than 3 lines of code to fix these errors; however, all the code changes
required are minor. (In other words, you will not have to make major changes
like changing indentation levels of code.)

### Step 4: Reflection

In your evaluation document, write a few paragraphs reflecting on your
experience in this lab.  You may want to consider questions such as:

* What was the most difficult error to debug?  How did you go
  about investigating it?
* What did you learn from this lab?  Has your approach or attitude
  towards debugging changed as a result of this lab?  If so,
  how?

## What to Hand In

* Evaluation document (should contain answers from Steps 2 and 4)
* Corrected `sum-practice.py` (with comments explaining fixes)
* Corrected `guess.py` (with comments explaining fixes)

## Grading

* To earn a C, submit a corrected version of `sum-practice.py`.
* To earn a B, do the above and submit an evaluation document with
  answers to the questions about the reading.
* To earn an A, do the above and submit a corrected version
  of `guess.py`.
* To earn a 100, do the above and complete the reflection in Step
  4.
