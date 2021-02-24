---
layout: work
type: Lab
num: 6
worktitle: Mutation is the Word
---

## Overview

In this lab we will make extensive use of while loops and strings.  We will explore
mutation of strings (words, DNA, ...) through playing the game Doublets.

## Materials
* [Common English Words](../data/english3.txt)
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

### Step 1 - Develop Pseudocode (3 points)

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

### Step 2 - Implement Incrementally (3 points)

Now take your pseduocode description and begin to implement your
program in Python.  Your program should be
named `doublets.py`.  Write your code in small sections and
test incrementally. **Never write more than 5-10 lines of code without
testing your changes!**  For example, you might start by making the
program ask the user for a starting word.  Once you have verified that
this part runs successfully and behaves how it is supposed to, you can
add the next part, and so on.

Be sure you can successfully play a game of Doublets with your
program, as shown in the example above, before moving on to Step 3.

### Step 3 - Error Handling and Function Decomposition (10 points total)

Of course the user might not always enter input in the expected form.
In this step, you will incrementally modify your program to ensure that 
the user only enters valid input. Building a program with robust error
handling is much easier if it is decomposed into functions, so we will
introduce error handling and functions into our program together.

#### Step 3.1 - Starting function decomposition (1 point)
First, place all of your code from Step 2 into a function named `main()`. 
It should look something like this:

    def main():
      ...

    main()
	
#### Step 3.2 - Starting word validation (2 points)
Next, write a function that ensures that the user inputs a valid word. 
For English word validation, download the text file [`english3.txt`](../data/english3.txt)
and the python module [`dictionary.py`](../code/dictionary.py) files, and
make sure they are in the same folder where you will put your lab. (To download these files,
you will need to right-click on them. A regular click will display their contents in your
browser.) You **do not need to copy and paste** anything!  At the top of your
Python program, you should put

    import dictionary

which will allow you to use the functions in `dictionary.py`.

The dictionary module contains a function
`valid_word(word, file)`, which will
return `True` if the word is found in the file and `False`
otherwise.  You can call the function by writing something like

    dictionary.valid_word(some_word, 'english3.txt')
	
Handling erroneous input requires using a loop. The following example shows
a loop structure that you may find helpful:

	valid = False
	while not valid:
		word = input("Enter a word that is at least four letters long: ")
		if len(word) >= 4:
			valid = True
		else:
			print(f"{word} is less than four letters long. Please try again.")
			
Use your function to ensure that the starting word is valid. Here is an example
of how the program would behave with the error checking in place:

    What is the starting word? lig
	lig is not a word. Please try again.
	What is the starting word? log
    What is the ending word?

#### Step 3.3 - Ending word validation (1 point)
Write a function to validate the ending word. This will be a slightly more complex 
variation of the function you wrote in Step 3.2, as it must ensure not only that 
the word is valid, it must also ensure that the word is of the same length as the
starting word. 

Use your function to ensure that the ending word is valid and of the correct length. Here is 
a continuation of our earlier example to show how the program should behave:

	What is the starting word? log
    What is the ending word? worm
    The lengths are not equal. Please try again.
    What is the ending word? sku
    sku is not a word. Please try again.
    What is the ending word? bug
    Start   = LOG
    Current = LOG
    End     = BUG
    Which character do you want to change? (the first character is 1)
	
#### Step 3.4 - Character index validation (2 points)
Write a function to validate the user's input of a character index to change. 
It should return an integer between 1 and the length of the current word. Any 
non-integer or any integer outside that range should result in a message to 
the user requesting suitable input. 

Use your function to ensure that the character index is valid. Here is 
a continuation of our earlier example to show how the program should behave:
	
	Start   = LOG
    Current = LOG
    End     = BUG
    Which character do you want to change? (the first character is 1) 0
    0 is out of range. Please try again.
    Which character do you want to change? (the first character is 1) 4
    4 is out of range. Please try again.
    Which character do you want to change? (the first character is 1) x
    x is not a number. Please try again.
    Which character do you want to change? (the first character is 1) 1
    What is your new character?
	
#### Step 3.5 - Character validation (2 points)
Write a function to ensure that the user inputs a single character. Here
is a continuation of our earlier example to show how the program should
behave once you are using your function:

    Which character do you want to change? (the first character is 1) 1
    What is your new character? bb
	bb is more than one character. Please try again.
    What is your new character? b
	Current = BOG
    End     = BUG
    Which character do you want to change? (the first character is 1)
	
#### Step 3.6 - Word validation (2 points)
Unlike the other error-handling steps, this step is straightforward to
implement without writing an additional function. Before committing
to the new word with the new character, make sure the new word is a 
valid word, again using the `dictionary` module. If it is a valid word,
update your current word, the number of steps, and the solution path.
If not, print an error message. In either case, the program will resume
at the top of the `while` loop.

Here is a continuation of our earlier example with this error-checking
in place:

	Current = BOG
    End     = BUG
    Which character do you want to change? (the first character is 1) 2
	What is your new character? 4
	B4G is not a valid word
	Current = BOG
	End     = BUG
	What character do you want to change? (the first character is 1) 2
	What is your new character? u
	solution path found in 2 steps.
	LOG -> BOG -> BUG

### Step 4 - Play (2 points)

Once your program is working, try out some of the transformations below:

* FIRE -- HEAT
* SLEEP -- DREAM
* APE -- MAN
* WHITE -- BLACK

What is the minimum number of steps you can achieve for each?

### Future Thoughts (2 points)

Your `doublets.py` program lets the user chose what character to change at each step,
and then verifies that each new word is a valid word.  Can you think of a way to always find the
minimum number of steps to transform one word to another?  How will you know if a path
between two words can be found? Include your answers to these questions
in the `Evaluation Document`.

## What to Hand In

<!--Make sure you have followed the [Python Style Guide](../python_style_guide.html), and
have run your project through the Automated Style Checker.-->
Make sure you examine all of the style suggestions that PyCharm makes, and adjust your code accordingly.

You must hand in:

* Evaluation Document (containing pseudocode, and answers to
	"Future thoughts" questions)
* `doublets.py`
* `dictionary.py`
* `english3.txt`

(Yes, please turn in `dictionary.py`
and `english3.txt` even though you did not create them---it makes
the grading process much easier!)

