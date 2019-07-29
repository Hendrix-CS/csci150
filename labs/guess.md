---
layout: work
number: CSCI 150
title: Foundations of Computer Science
semester: Fall 2019
---
# Lab 5: Guess My Number

## Overview

In this lab, you will practice using `while` loops in
Python by implementing the classic game "Guess My Number".

Be sure to **read carefully!** This lab writeup has lots of hints
and instructions to help you along the way.

## Step 1

For the first step, you will implement a basic version of the game.
Here is what a sample run of the program might look like:


    Welcome to guess the number!
    I will pick a number from 1-100, and you try to guess it.
    I will tell you whether each guess is too low or too high.
    ...OK, I have picked a number.
    Your guess? 50
    50 is too low.
    Your guess? 60
    60 is too high.
    Your guess? 65
    65 is too high.
    Your guess? 61
    61 is too high.
    Your guess? 55
    55 is too high.
    Your guess? 51
    You got it!  It took you 6 guesses.


Start by creating a file called `guess_number.py` and **paste
the following code into it**:

    ######################################
    # Copyright (c) 2019 YOUR NAME(s) HERE
    # CSCI 150, Spring 2019
    # Lab 5: Guess My Number
    ######################################

    import random

    def main():
        # Write your code here

    # Call main() as the last thing in the file
    main()

Update it with your name. **Inside the `main()` function**,
you should implement the game as illustrated above.

* Use `random.randint(1,100)` to pick a random number
between 1 and 100.
* Of course you will need a `while` loop to keep
prompting the user for their guess.  As the loop control variable,
you can use either the user's guess itself, or you can create a
sentinel variable which starts as `False` and
becomes `True` once the user has correctly guessed the
number.
* As in the Collatz example in class, you will need to use a
separate counter variable to keep track of the number of guesses.

## Step 2

Your game works now, but it has a problem:

    Welcome to guess the number!
    I will pick a number from 1-100, and you try to guess it.
    I will tell you whether each guess is too low or too high.
    ...OK, I have picked a number.
    Your guess? fifty
    Traceback (most recent call last):
      File "guess_number.py", line 33, in <module>
        main()
      File "guess_number.py", line 22, in main
        guess = int(input("Your guess? "))
    ValueError: invalid literal for int() with base 10: 'fifty'

If the user enters invalid input, the program will crash.  We have
noted this problem before, but now that we know how to do repetition,
we can actually do something about it!


You should write a new function called `input_guess()`.  Here is a
template you can use as a starting point; copy it into your file
(after `import random` and before `def main():`):

    # input_guess prompts the user for their guess, and keeps prompting
    # until it is valid.
    #
    # Input:  none
    # Output: a valid guess (int)
    def input_guess() -> int:
        # Keep prompting the user for their guess until they enter
        # something valid

        # FILL IN CODE HERE

        # We only do this conversion at the end, once we know
        # guess_str looks like an int
        guess: int = int(guess_str)

        # Finally, return the user's guess
        return guess

Be sure that the comments and the `def` start all the way
over in the leftmost column of your file (do **not** put it inside
your `main()` function!).


If the user's input is stored as a string in the
variable `guess_str`, you can check whether it is valid
using `guess_str.isdigit()`, which is a True or False value
telling you whether the string `guess_str` consists of all
digits or not.


Finally, replace the part of your `main()` function that
asks the user for their input with a call to your
new `input_guess()` function.  That is, instead of
something like

    guess: int = int(input("Your guess? "))

you should now have

    guess: int = input_guess()

Here's what the output of your program might look like once you
complete this step:

    Welcome to guess the number!
    I will pick a number from 1-100, and you try to guess it.
    I will tell you whether each guess is too low or too high.
    ...OK, I have picked a number.
    Your guess? fifty
    fifty is not a number.  Try again.
    Your guess? iuerhuheg
    iuerhuheg is not a number.  Try again.
    Your guess? 20
    20 is too low.

If you like, you may also modify `input_guess()` so that it
ensures the user's guess is between 1 and 100, but this is not required.

## Step 3

Since this game is so addictive, it's inconvenient to re-run it every
time we want to play.  In this step, you will modify the game so that
the user can keep playing multiple rounds until they decide to stop.


You should put another `while` loop around an appropriate
part of your `main()` function so that it will repeat the
entire game until the user wants to stop.  Here is what the output of
your program might look like once you get this to work:

    Welcome to guess the number!
    I will pick a number from 1-100, and you try to guess it.
    I will tell you whether each guess is too low or too high.
    ...OK, I have picked a number.
    Your guess? 50
    50 is too low.
    Your guess? 70
    70 is too high.
    Your guess? 60
    60 is too high.
    Your guess? 55
    You got it!  It took you 4 guesses.
    Would you like to play again? (yes/no) yes
    ...OK, I have picked a number.
    Your guess? 20
    20 is too low.
    Your guess? 80
    80 is too high.
    Your guess? 05
    5 is too low.
    Your guess? 50
    50 is too high.
    Your guess? 30
    30 is too high.
    Your guess? 25
    25 is too high.
    Your guess? 23
    You got it!  It took you 7 guesses.
    Would you like to play again? (yes/no) no

## Step 4

Finally, create a new file called `computer_guess.py`.  You
should implement the same game, but with the roles reversed!  That is,
the human user picks a number, and the computer tries to guess it.
Here is an example of what your program's output might look like:

    Welcome to guess the number!  You pick a number from 1-100
    and I will guess it.  Please tell me whether my guesses are
    "correct", "low", or "high".
    Is your number 50? too high
    Please respond with "correct", "low", or "high".
    Is your number 50? erogiherg
    Please respond with "correct", "low", or "high".
    Is your number 50? high
    Is your number 25? high
    Is your number 12? low
    Is your number 18? low
    Is your number 21? high
    Is your number 19? low
    Is your number 20? correct
    Yay!  I win!  It only took me 7 guesses.
    Shall we play again? (yes/no) yes
    Is your number 50? low
    Is your number 75? low
    Is your number 88? high
    Is your number 81? high
    Is your number 78? correct
    Yay!  I win!  It only took me 5 guesses.
    Shall we play again? (yes/no) no

A few hints:

  * Be sure that your program responds appropriately if the user
    inputs something unexpected, as in the example above.
  * Your program should offer the option of playing again as long as
    the user wants to continue playing.
  * Feel free to just put everything inside a `main()`
    function; you need not worry about writing any functions for this step.

## What to turn in

  * `guess_number.py`
  * `computer_guess.py`

**Remember to follow** the
[Python style guide](http://mgoadric.github.io/csci150/python_style_guide.html)
and to run the style checker before turning in your programs!

## Grading

* To earn a C, complete step 1.
* To earn a B, complete steps 1, 2, and 3.
* To earn an A, complete steps 1-4.
* To earn a 100, make sure the computer never needs more than 7 guesses to win!
