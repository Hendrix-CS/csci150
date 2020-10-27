---
layout: work
type: Lab
num: 10
worktitle: Waterjugs
---

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

## Step 1: The `WaterJug` class (8 points total)

Open a file named `waterjug.py`. In this file, you will define
the `WaterJug` class.

### Writing the WaterJug class (4 points)

Each `WaterJug` object will need to have two variables
that we can think of as the state of that `WaterJug`:

  * an `int` for `capacity`
  * an `int` for `contents`

Also, a `WaterJug` needs some functionality to change the state of the internal components.
In object-oriented programming, these are called methods.

Methods:

  * `__init__(self, capacity: int, contents: int)` constructor method
  * `__repr__(self)` returns a string representing the value of the `WaterJug` object
  * `fill(self)` to fill up the `WaterJug` completely
  * `empty(self)` to completely empty the `WaterJug`
  * `pour(self, other: 'WaterJug')` to pour as much of the contents of this `WaterJug` into the other as is allowed

Implement this class in Python.

{% include warning.html content="Be careful with your methods to make
sure a malicious programmer (or buggy code) cannot violate the
integrity of your class.  For example, it should never be possible
to end up with a `WaterJug` with more `contents`
than `capacity`." %}

{% include tip.html content="Don't forget where to use the `self` keyword." %}

### Testing the WaterJug class (4 points)

At the end of your file, place the following lines of code:

    if __name__ == '__main__':
        test()

Above that, write a function named `test()` that tests
your class and ensures that it works.  Make sure your test code uses all
of the methods of the class.  

For each test, write an *assertion* using Python's `assert` statement. 
An assertion is a claim that a given statement is true. If the statement 
is not true, the program ends with an error message. Here are some examples:

	jugA = WaterJug(4, 0)
	assert jugA.capacity == 4
	assert jugA.contents == 0

If all tests pass, it should print a success message.

One approach to creating a good test function is to write code that
simulates the six actions above with Jugs A and B that leaves 2 gallons
of water in Jug A.

The `__repr__` method needs to return a string that, if
typed into the Python shell, would reconstruct the original object.
The `str` function calls `__repr__` for its argument
in order to create its string representation. The `eval`
function calls the Python interpreter to execute its string argument.
The following function will test whether `__repr__` works for
any class:

    def test_repr(obj):
        return str(obj) == str(eval(str(obj)))

## Step 2: The Puzzle (6 points)

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
	     * fill A, fill B
		 * empty A, empty B
		 * pour A B, pour B A
	 * Ask the user for their option selection
	 * Perform the selected option
* When the goal is met, print the solution path found by the user
to reach the goal. You will need to maintain this solution path
using a list or a string.

Here is an example run of the program for you to emulate:

	Enter the capacity of Jug A: 4
	Enter the capacity of Jug B: 3
	Enter the goal quantity of water for Jug A: 2
	A: WaterJug(4,0) B: WaterJug(3,0)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): fill A
	A: WaterJug(4,4) B: WaterJug(3,0)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): pour A B
	A: WaterJug(4,1) B: WaterJug(3,3)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): empty B
	A: WaterJug(4,1) B: WaterJug(3,0)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): pour A B
	A: WaterJug(4,0) B: WaterJug(3,1)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): fill A
	A: WaterJug(4,4) B: WaterJug(3,1)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): pour A B
	Goal achieved!
	fill A
	pour A B
	empty B
	pour A B
	fill A
	pour A B

{% include important.html content="Do not just put everything in `main`.
You should break your code up into functions appropriately." %}

{% include note.html content="It is not necessary to validate user input. For this
assignment, you may assume that all user input is valid." %}

## Step 3: Generalizing (6 points)

In a new file, `step3.py`, generalize your program from Step 2 so
that it works with any number
of `WaterJug`s instead of just 2.  In particular, the
program should:

* Ask the user how many `WaterJug`s they want
* Prompt them for the capacity of each
* ...and so on

If any of the jugs reaches the goal amount, the program should congratulate
the user, print the solution path, and end.

Here is an example run for your program to emulate:

	How many jugs? 3
	Enter capacity for jug 0: 4
	Enter capacity for jug 1: 4
	Enter capacity for jug 2: 5
	What is the goal amount (for any jug)? 2
	Jug 0: WaterJug(4,0)
	Jug 1: WaterJug(4,0)
	Jug 2: WaterJug(5,0)
	Enter command (fill, empty, pour) followed by jug number(s): fill 2
	Jug 0: WaterJug(4,0)
	Jug 1: WaterJug(4,0)
	Jug 2: WaterJug(5,5)
	Enter command (fill, empty, pour) followed by jug number(s): pour 2 0
	Jug 0: WaterJug(4,4)
	Jug 1: WaterJug(4,0)
	Jug 2: WaterJug(5,1)
	Enter command (fill, empty, pour) followed by jug number(s): pour 2 1
	Jug 0: WaterJug(4,4)
	Jug 1: WaterJug(4,1)
	Jug 2: WaterJug(5,0)
	Enter command (fill, empty, pour) followed by jug number(s): fill 2
	Jug 0: WaterJug(4,4)
	Jug 1: WaterJug(4,1)
	Jug 2: WaterJug(5,5)
	Enter command (fill, empty, pour) followed by jug number(s): pour 2 1
	Congratulations! Goal achieved.
	fill 2
	pour 2 0
	pour 2 1
	fill 2
	pour 2 1

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
