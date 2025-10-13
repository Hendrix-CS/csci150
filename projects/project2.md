---
layout: work
type: Project
num: 2
worktitle: Word Games
---

**Due Wednesday, October 29**
## Description

For this project, you will create a program for users to play a [word
game](http://en.wikipedia.org/wiki/Word_game) of your choice.

In particular, your project should be complex enough that it includes
several of the following concepts we have discussed in class:

*   Booleans
*   Functions
*   Conditional statements
*   Loops
*   Strings
*   Lists
*   File input/output

(It is not an absolute requirement for your program to contain every
single one of the above elements; but if it does not need most of them,
then your program is probably not interesting/complex enough.) The game
can be for one person against a computer, or two players against each
other.

Some examples include:

*   [Bulls and Cows](http://en.wikipedia.org/wiki/Bulls_and_cows)
    (using **words**, not numbers) or [Wordle](https://en.wikipedia.org/wiki/Wordle)
*   [Hangman](https://en.wikipedia.org/wiki/Hangman_(game))
*   [Ghost](http://en.wikipedia.org/wiki/Ghost_%28game%29)
*   [Wheel of Fortune](https://en.wikipedia.org/wiki/Wheel_of_Fortune_(American_game_show))
    * No need for three players or an animated wheel.
*   [Boggle](http://en.wikipedia.org/wiki/Boggle)
*   [Prolix](http://boardgamegeek.com/boardgame/39635/prolix)
*   a program to let a user solve a
    [Cryptogram](http://en.wikipedia.org/wiki/Cryptogram)
*   [Last Letter First
    Letter](http://www.greatschools.org/students/activities/slideshows/2812-family-word-games.gs?page=3)
    using countries, state names, foods, etc.

**Do not feel limited by the games on this list**. Find a word game that
interests you and implement it. If you choose something else, check with
one of your instructors first, so we can advise you on the scope of your project.

## Requirements

Your program should explain the game to the user, being clear exactly
what input is expected and valid whenever requesting information from
them.

The user must be able to

* choose a level of difficulty for the game,

* be offered the chance to play the game again when finished, and

* make mistakes in entry of information and be prompted to correct their
input.

**Your code must make good use of functions**. Using functions will reduce
the amount of code you need to write as well as make your program easier
to debug. However, do not write [spaghetti
code](http://en.wikipedia.org/wiki/Spaghetti_code), where functions call
each other back and forth to continue execution of the program; let your
functions naturally return values and use loops to repeat the game
turns.

## Warnings

*   **Get started early**! Pick a game and run it by us. We are happy to
    help you think through the design of your program.
*   If you are not confident with the use of functions to structure your
    code, we highly recommend *first* getting something very basic to
    work without using functions, then thinking about how to abstract
    parts of your code into functions. Then repeat the process, adding
    functionality incrementally.
*   Historically, project 2 is the point in the semester where some
    students become **tempted to cheat** by copying others' code. Do
    not succumb to this temptation! Review the [Academic
    Integrity](http://ozark.hendrix.edu/~yorgey/ac-integrity-policy.html)
    guidelines for CSCI. Get started early, come for help often.  You
    **can** do this project!

## What to Hand In

You must hand in all files necessary to run your code.


## Grading Criteria
* A **Level 1** project:
  * Explains the game to the user, making clear exactly what input
    is expected and valid whenever it requests information from them.
  * Enables the human player to play a word game to completion without any errors.
  * The word game is complex enough to employ at least **three** of the concepts from the list above.
* A **Level 2** project meets the criteria for **Level 1**, and meets the following additional criteria:
  * The word game is complex enough to employ at least **five** of the concepts from the list above.
  * Has at least three levels of difficulty.
  * Offers the chance to play the game again when finished.
  * Enables the user to correct mistakes in the entry of information.
  * Makes good use of functions to structure the project.
    - Functions are relatively short and conceptually do a single job
    - Functions are used to hierarchically decompose the program
