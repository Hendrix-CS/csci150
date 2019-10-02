---
layout: work
number: CSCI 150
title: Foundations of Computer Science
semester: Fall 2019
---
# Lab 6: Mutation is the Word

## Overview

In this lab we will make extensive use of while loops and strings.  We will explore
mutation of strings (words, DNA, ...) through playing the game Doublets.

## Materials
* [Common English Words](../data/english2.txt)
* [dictionary.py](../code/dictionary.py) Python Module
* Lab Partner

## Description

[Charles Lutwidge Dodgson](http://en.wikipedia.org/wiki/Lewis_Carroll) (aka
Lewis Carroll), who is most famous for his novel "Alice in Wonderland",
introduced a puzzle called Doublets in an article for
*Vanity Fair*.  His rules description is as follows:

>The rules of the Puzzle are simple enough. Two words are proposed, of the same length;
and the Puzzle consists in linking these together by interposing other words,
each of which shall differ from the next word in one letter only. That is to say,
one letter may be changed in one of the given words, then one letter in the word so
obtained, and so on, till we arrive at the other given word. The letters must not be
interchanged among themselves, but each must keep to its own place. As an example,
the word 'head' may be changed into 'tail' by interposing the words
'heal, teal, tell, tall'. I call the given words 'a Doublet', the interposed words
'Links', and the entire series 'a Chain', of which I here append an example:

    H E A D
    h e a l
    t e a l
    t e l l
    t a l l
    T A I L

>It is, perhaps, needless to state that it is de rigueur that the links should be
English words, such as might be used in good society.

(More details on the connection between Lewis Carroll and genetics can be found in an article by
David B. Searls entitled
[From *Jabberwocky* to Genome: Lewis Carroll and Computational Biology](http://www.liebertonline.com/doi/abs/10.1089/10665270152530881).

Our task for this lab is to create a Python program that lets a user play the Doublets game
and enforces all the rules given above by Lewis Carroll.

### Step 1 - Develop Pseudocode

Develop an algorithmic solution using
*pseudocode*.  This should correspond to the structure of a
Python program, but is written in English instead of Python.

For example, pseudocode for a guessing-game could look like this:

    Generate a number for the human to guess
    While the human has not guessed the number:
        Request a guess from the human
        If it's too high or too low, say so
    Congratulate the human on their insight

The point is that this is *structured* like Python, using indentation
and hinting at loops and conditionals.  But the individual pieces are
just English descriptions, which you will later translate into precise
Python code.  You do **not** need to use any functions at this
point---we will do that later.

To demonstrate the eventual behavior of the program, here is a
sample run of the Doublets game. For now, do not worry about what
should happen if the user enters invalid input; assume that the user
will always enter exactly what is expected.

    What is the starting word? CAT
    What is the ending word? DOG
    Start   = CAT
    Current = CAT
    End     = DOG
    Which character do you want to change? (the first character is 1) 3
    What is your new character? B
    Current = CAB
    End     = DOG
    Which character do you want to change? (the first character is 1) 2
    What is your new character? O
    Current = COB
    End     = DOG
    Which character do you want to change? (the first character is 1) 3
    What is your new character? G
    Current = COG
    End     = DOG
    Which character do you want to change? (the first character is 1) 1
    What is your new character? D
    Solution path found in 4 steps.
    CAT -> CAB -> COB -> COG -> DOG

### Step 2 - Implement Incrementally

Now take your pseduocode description and begin to implement your
program in Python.  Your program should be
named `doublets.py`.  Write your code in small sections and
test incrementally. **Never write more than 5-10 lines of code without
testing your changes!**  For example, you might start by making the
program ask the user for a starting word.  Once you have verified that
this part runs successfully and behaves how it is supposed to, you can
add the next part, and so on.

### Step 3 - Error Handling

Of course the user might not always enter input in the expected form.
A second run of the program is shown below, where the user made many
mistakes.

    What is the starting word? log
    What is the ending word? worm
    The lengths are not equal. Please try again.
    What is the ending word? sfu
    sfu is not a word. Please try again.
    What is the ending word? bug
    Start   = LOG
    Current = LOG
    End     = BUG
    Which character do you want to change? (the first character is 1) 0
    0 is out of range. Please try again.
    Which character do you want to change? (the first character is 1) 4
    4 is out of range. Please try again.
    Which character do you want to change? (the first character is 1) 1
    What is your new character? 4
    4og is not a valid word
    Current = LOG
    End     = BUG
    Which character do you want to change? (the first character is 1) 1
    What is your new character? b
    Current = BOG
    End     = BUG
    Which character do you want to change? (the first character is 1) x
    x is not a number. Please try again.
    Which character do you want to change? (the first character is 1) 2
    What is your new character? uu
    uu is more than one character. Please try again.
    Which character do you want to change? (the first character is 1) 2
    What is your new character? u
    Solution path found in 2 steps.
    LOG -> BOG -> BUG

Modify your program so that it is able to gracefully handle erroneous
input, as illustrated above.  The goal is to have a program
that **never** crashes, no matter what the user enters.

For English word validation, download the text file [`english2.txt`](../data/english2.txt)
and the python module
[`dictionary.py`](../data/dictionary.py) files, and
make sure they are in the same folder where you will put your lab.
You **do not need to copy and paste** anything!  At the top of your
Python program, you should put

    import dictionary

which will allow you to use the functions in `dictionary.py`.

The dictionary module contains a function
`valid_word(word, file)`, which will
return `True` if the word is found in the file and `False`
otherwise.  You can call the function by writing something like

    dictionary.valid_word(some_word, 'english2.txt')

### Step 4 - Function Decomposition

Once your program is working, go through the process of abstracting
out parts of the program into functions, as illustrated in class.  By
the end, your program should be structured **entirely using
functions**; that is, your program should look something like this:

    # Input: ...
    # Output: ...
    # Description
    def fun1(x,y,z):
      ...

    ... More functions here with appropriate comments ...

    def main():
      ...

    main()

### Step 5 - Play

Once your program is working, try out some of the transformations below:

* FIRE -- HEAT
* SLEEP -- DREAM
* APE -- MAN
* WHITE -- BLACK

What is the minimum number of steps you can achieve for each?

### Future Thoughts

Your `doublets.py` program lets the user chose what character to change at each step,
and then verifies that each new word is a valid word.  Can you think of a way to always find the
minimum number of steps to transform one word to another?  How will you know if a path
between two words can be found? Include your answers to these questions
in the `Evaluation Document`.

## What to Hand In

Make sure you have followed the [Python Style Guide](../python_style_guide.html), and
have run your project through the Automated Style Checker.

You must hand in:

* Evaluation Document (containing pseudocode, and answers to
	"Future thoughts" questions)
* `doublets.py`
* `dictionary.py`
* `english2.txt`

(Yes, please turn in `dictionary.py`
and `english2.txt` even though you did not create them---it makes
the grading process much easier!)

## Grading

* To earn a D, turn in an Evaluation Document.
* To earn a C, do the above and implement a program that can handle
  the input in the first sample run.
* To earn a B, implement a program that can handle the input in the
  first sample run, and is entirely well-decomposed into functions.
* To earn a A, do the above and implement a program that can handle
  the input in the second sample run.
* To earn a 100, do the above and follow the style guide exactly.
