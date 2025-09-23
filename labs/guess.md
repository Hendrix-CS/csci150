---
layout: work
type: Lab
num: 4
worktitle: Guess My Number
---

## Overview

In this lab, you will practice using `while` loops in
Python by implementing the classic game "Guess My Number".

Be sure to **read carefully!** This lab writeup has lots of hints
and instructions to help you along the way.

## Step 0: Getting started

In this and the following labs, we will be creating interactive programs
that require user input. [PyCharm](https://www.jetbrains.com/pycharm/) is an
[IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)
that lets us write these types of programs in Python.

Open PyCharm and create a new project (by going to the <kbd>File</kbd> menu
and selecting <kbd>New Project</kbd>).  Name it `labs_150`.
Accept the other defaults and click <kbd>Create</kbd>.

At this point you will have a new, empty project.  Each project can
contain multiple Python files.  To create a new Python file, you can
either choose <kbd>New...</kbd> under the <kbd>File</kbd> menu, or right click on the
project folder and select <kbd>New...</kbd>.  Make sure you select <kbd>New
Python File</kbd>.  Then you can type in a name for the file.  Note that
you should not include `.py` on the end of the name;
PyCharm will add `.py` for you.

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

    import random


    def main():
        # Write your code here


    # Call main() as the last thing in the file
    main()

**Inside the `main()` function**,
you should implement the game as illustrated above.

* Use `random.randint(1, 100)` to pick a random number
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

    def input_guess() -> int:
        # input_guess prompts the user for their guess, and keeps prompting
        # until it is valid.
        #
        # Input:  none
        # Output: a valid guess (int)
        # Keep prompting the user for their guess until they enter
        # something valid

        # FILL IN CODE HERE

        # We only do this conversion at the end, once we know
        # guess_str looks like an int
        guess = int(guess_str)

        # Finally, return the user's guess
        return guess

Be sure that the comments and the `def` start all the way
over in the leftmost column of your file (do **not** put it inside
your `main()` function!).

{% include tip.html content="If the user's input is stored as a string in the
variable `guess_str`, you can check whether it is valid
using `guess_str.isdigit()`, which is a Boolean (`True` or `False`) value
telling you whether the string `guess_str` consists of all
digits or not." %}

Finally, replace the part of your `main()` function that
asks the user for their input with a call to your
new `input_guess()` function.  That is, instead of
something like

    guess = int(input("Your guess? "))

you should now have

    guess = input_guess()

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

First, create a new function called `run_game()`. It will not have
any parameters nor will it return any value. Cut and paste the part
of `main()` that begins with generating the random number to
guess and ends with printing the number of guesses into this
new function. Then place a call to `run_game()` in `main()` where
that code used to be. Test the program and ensure it still works.

Next, write a new `while` loop in `main()`. Inside the loop,
call `run_game()` to play one round of the game. Then, ask the
user whether they wish to play again. The loop should end if the
user does not wish to play again.  Here is what the output of
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

Finally, create a new file called `computer_guess.py`. Starting with
the template provided in step 1, implement the same game, but with
the roles reversed!  That is, the human user picks a number, and the
computer tries to guess it.
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
  * Write a `play_once()` function that plays one round of the game.
  * In `main()`, call `play_once()` from within a `while` loop that
	asks the user whether they wish to play again, much as we did
	in Step 3.
  * Do **not** use a random number to generate the computer's guess.
    The computer's strategy should be systematic and deterministic.

## Optional Step 5:

Modify your strategy from Step 4 to ensure that the computer *never*
needs more than 7 guesses to win!
