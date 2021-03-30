---
layout: work
type: Lab
num: 9
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
jugs, A and B, and an inexhaustible supply of water. There are three
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

## Step 1: The `WaterJug` class (10 points)

Open a file named `waterjug.py`. In this file, you will define
the `WaterJug` class. Each `WaterJug` object will need to have two variables
that we can think of as the state of that `WaterJug`:

  * an `int` for `capacity`
  * an `int` for `contents`

Also, a `WaterJug` needs functions to change the state of the internal components.
In object-oriented programming, these functions are called **methods**.

Methods:

  * `fill(self)` to fill up the `WaterJug` completely
  * `empty(self)` to completely empty the `WaterJug`
  * `pour(self, other: 'WaterJug')` to pour as much of the contents of this `WaterJug` into the other as is allowed

Implement this class in Python. Here is an incomplete implementation you can use 
as a guide:

	from dataclasses import dataclass


	@dataclass
	class WaterJug:
		capacity: int
		contents: int

		def fill(self):
			pass # Your code here

		def empty(self):
			pass # Your code here

		def pour(self, other: 'WaterJug'):
			pass # Your code here


	def test():
		jugA = WaterJug(4, 0)
		jugB = WaterJug(3, 0)
		jugA.fill()
		assert jugA.capacity == 4
		assert jugA.contents == 4
		jugA.pour(jugB)
		assert jugA.contents == 1
		assert jugB.contents == 3
		assert jugA.capacity == 4
		assert jugB.capacity == 3
		jugB.empty()
		assert jugB.contents == 0
		assert jugB.capacity == 3
		jugA.pour(jugB)
		assert jugA.contents == 0
		assert jugB.contents == 1
		jugA.fill()
		jugA.pour(jugB)
		assert jugA.contents == 2
		assert jugB.contents == 3
		print("All tests passed")


	if __name__ == '__main__':
		test()
	


{% include warning.html content="Be careful with your methods to make
sure a malicious programmer (or buggy code) cannot violate the
integrity of your class.  For example, it should never be possible
to end up with a `WaterJug` with more `contents`
than `capacity`." %}

{% include tip.html content="Don't forget where to use the `self` keyword." %}

### Testing the WaterJug class 

At the end of your file, we included some tests. The test code uses all
of the methods of the class.  

Each test uses Python's `assert` statement to determine if the code is correct 
at that point. An assertion is a claim that a given statement is true. If the 
statement is not true, the program ends with an error message. Here are some 
examples:

	jugA = WaterJug(4, 0)
	assert jugA.capacity == 4
	assert jugA.contents == 0

If all tests pass, it will print a success message. If any of the assertions fail,
you will see an appropriate message. For example, if you were to test the incomplete
code above, the first assertion would fail, and you would get something like 
the following message:

	Traceback (most recent call last):
	  File "C:/Users/ferrer/PycharmProjects/waterjug/waterjug.py", line 44, in <module>
		test()
	  File "C:/Users/ferrer/PycharmProjects/waterjug/waterjug.py", line 24, in test
		assert jugA.contents == 4
	AssertionError



## Step 2: The Puzzle (10 points)

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

	A: WaterJug(capacity=4, contents=0) B: WaterJug(capacity=3, contents=0)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): fill A

	A: WaterJug(capacity=4, contents=4) B: WaterJug(capacity=3, contents=0)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): pour A B

	A: WaterJug(capacity=4, contents=1) B: WaterJug(capacity=3, contents=3)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): empty B

	A: WaterJug(capacity=4, contents=1) B: WaterJug(capacity=3, contents=0)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): pour A B

	A: WaterJug(capacity=4, contents=0) B: WaterJug(capacity=3, contents=1)
	Enter your choice: fill (A,B); empty (A,B); pour (A B, B A): fill A

	A: WaterJug(capacity=4, contents=4) B: WaterJug(capacity=3, contents=1)
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

You never know when a Python class could save your life.  And
remember, "Think fast, Look alive, Die hard."

## What to Hand In

You must hand in:

  * `waterjug.py`
  * `step2.py`
