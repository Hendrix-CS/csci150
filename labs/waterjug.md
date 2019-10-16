---
layout: work
---
# Lab 10 : Water Jugs

## Overview

This lab will combine
mathematics, instantiable classes, and bone-chilling terror. ;) Always
a famous puzzle in the Artifical Intelligence circles, the
[WaterJug](https://www.youtube.com/watch?v=BVtQNK_ZUJg)
came to popular culture through the classic action movie
[Die Hard III](http://us.imdb.com/Title?Die+Hard%3A+With+a+Vengeance+(1995)).
In Die Hard III, a mad bomber is chasing Bruce Willis
and Samuel L. Jackson.  They must solve different puzzles or else
things will explode and people will die.

### Example
The WaterJug puzzle can be explained as follows:

You have two
jugs, A and B, and an infinite supply of water. There are three
actions you can perform: (1) you can fill a jug to capacity, (2) you
can completely empty a jug, and (3) you can pour from one jug to the
other.  Pouring from one jug to the other stops when the first jug
is empty or the second jug is full, whichever comes first. For
example, if A has 5 gallons and B has 6 gallons and a capacity of 8,
then pouring from A to B leaves B full and 3 gallons in A.

For this demonstration, we'll state that A has capacity 4 and
B has capacity 3.  Our goal, which we must complete in less than one
minute, is to somehow get exactly 2 gallons of water in jug A.  We need
to find a set of operations, filling, emptying, and pouring, where
we can reach this goal.  One possible solution is as follows:

    FILL A
    POUR from A to B
    EMPTY B
    POUR from A to B
    FILL A
    POUR from A to B

We now have exactly 2 gallons of water jug in A.  (Try it!).  Phew,
we're still alive!  Wouldn't it be nice to have a computer program
to help us solve this?

## Step 1: The `WaterJug` class

Each `WaterJug` object will need to have two variables
that we can think of as the state of that `WaterJug`:

  * an `int` for `capacity`
  * an `int` for `contents`

Also, a `WaterJug` needs some functionality to change the state of the internal components.
In object-oriented programming, these are called methods.

Methods:

  * `__init__(capacity: int, contents: int)` constructor method
  * `__repr__( )` returns a string representing the value of the `WaterJug` object
  * `fill()` to fill up the `WaterJug` completely
  * `empty()` to completely empty the `WaterJug`
  * `pour(other: 'WaterJug')` to pour as much of the contents of this `WaterJug` into the other as is allowed

Implement this object in Python. Don't forget where to use
the `self` keyword.  Be careful with your methods to make
sure a malicious programmer (or buggy code) cannot violate the
integrity of your class.  For example, it should never be possible
to end up with a `WaterJug` with more `contents`
than `capacity`.

Your code should go in a file named `waterjug.py`.
At the end of that file, place the following lines of code:

    if __name__ == '__main__':
        test()


Above that, write a function named `test()` that tests
your class and ensures that it works.  Make sure your test code uses all
of the methods of the class.  It should employ `if`
statements to check whether each test passes. If a test fails,
it should print an appropriate message. If all tests pass, it should
print a success message.

 The `__repr__` method needs to return a string that, if
typed into the Python shell, would reconstruct the original object.
The `str` function calls `__repr__` for its argument
in order to create its string representation. The `eval`
function calls the Python interpreter to execute its string argument.
The following function will test whether `__repr__` works for
any class:

    def test_repr(obj):
        return str(obj) == str(eval(str(obj)))

## Step 2: The Puzzle

In a new file, `step2.py`, write a program
that allows the user to set up and then solve a
water jugs puzzle.  To use the `WaterJug` class,
you will need the following line at the top of your file:

    from waterjug import WaterJug

Your program should:

* Ask the user the capacity of the first `WaterJug`
* Ask the user the capacity of the second `WaterJug`
* Ask the user the goal quantity of water
* Create the necessary empty `WaterJug` objects
* While the goal has not been met:
	 * Give the user a list of the options
	 * Ask the user for their option selection
	 * Perform the selected option
* When the goal is met, print the solution path found by the user
to reach the goal. You will need to maintain this solution path
using a list or a string.

**It is not necessary to validate user input.** For this
assignment, you may assume that all user input is valid.
Also, you should not just put everything in `main`,
but you should break your code up into functions appropriately.

## Step 3: Generalizing

In a new file, `step3.py`, generalize your program from Step 2 so
that it works with any number
of `WaterJug`s instead of just 2.  In particular, the
program should:

* Ask the user how many `WaterJug`s they want
* Prompt them for the capacity of each
* ...and so on

You never know when a Python class could save your life.  And
remember, "Think fast, Look alive, Die hard."

## What to Hand In
Make sure
you have followed the
[Python Style Guide](../python_style_guide.html), and
have run your project through the Automated Style Checker.

You must hand in:

  * `waterjug.py`
  * `step2.py`
  * `step3.py`
  *  Optional Lab Evalution Document (see Grading)

## Grading

* To earn a D on this lab, complete Step 1.
* To earn a B on this lab, do all the above and complete Step 2.
* To earn an A on this lab, do all the above and complete Step 3.
* To earn a 100 on this lab, do all the above and write a
paragraph explaining how you might write a Python program to
automatically play the WaterJug game.
