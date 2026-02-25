---
layout: work
type: Lab
num: 5
worktitle: Doublets
---

## Overview

In this lab we will make extensive use of while loops and strings
through the game Doublets.

## Materials
* <a href="../data/english3.txt" download>Common English Words</a>
* <a href="../code/spellcheck.py" download>`spellcheck.py`</a> Python Module
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

Your task for this lab is to create a Python program that lets a user play the Doublets game
and enforces all the rules given above by Lewis Carroll.

### Step 1 - Develop Pseudocode

Develop an algorithmic solution using
*pseudocode*.  This should correspond to the **structure** of a
Python program, but is written in English instead of Python.

For example, pseudocode for a guessing-game could look like this:

    Generate a number for the human to guess
    While the human has not guessed the number:
        Request a guess from the human
        If it's too high or too low, say so
    Congratulate the human

The point is that this is *structured* like Python, using indentation
and using things like loops and conditionals.  But the individual pieces are
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

Create a new Python file named `doublets.py` and write your pseudocode
in some comments.  Study the example above and try to write structured
pseudocode for a program that can play this game.

### Step 2 - Initial Implementation

#### Step 2.1 - `swap_character()`

Before turning your pseudocode into Python, let's first accomplish a
helpful subtask.  You should write a `swap_character()` function:

	def swap_character(word: str, where: int, updated: str) -> str:

Given a word (`word`), the index of a character in the word to replace
(`where`), and a new character to insert (`updated`), this function
should return a new string with the new character in place of the old
character. In keeping with our example transcript above, the `where`
variable will be an integer between 1 and the length of `word`.

To implement `swap_character()`:
* Use string slicing and string concatenation.
* Do **not** use a `while` loop.
* Do **not** use `input`. All of the input you need is given by the three parameters (`word`, `where`, and `updated`).

Here are a few examples. Test your implementation of
`swap_character()` in the Python Console with these examples:
* `swap_character("cat", 3, "r")` should return `"car"`
* `swap_character("track", 3, "u")` should return `"truck"`
* `swap_character("talk", 1, "w")` should return `"walk"`
* `swap_character("book", 3, "n")` should return `"bonk"`

#### Step 2.2 - Main program

Based on your pseduocode description, implement your program in
Python, within a function named `main()`. After prompting the user to
`input` the position to change and the new character to use, call
`swap_character()` to build the updated word. You should print the
number of solution steps, but you do not yet need to print the actual
chain of steps (you will add that in Step 2.3).

Your program structure should look something like this:

    def main():
      ...


	def swap_character(word: str, where: int, updated: str) -> str:
	  ...


    main()

Be sure you can successfully play a game of Doublets with your
program, as shown in the example above, before moving on to the next step.

#### Step 2.3 - Solution Path

Create a string variable to store the solution chain. It should initially be the starting
word. On each loop step, concatenate `" -> "` and the current word. Then print it out
at the end of the program.

### Step 3 - Error Handling and Function Decomposition

Of course the user might not always enter input in the expected form.
In this step, you will incrementally modify your program to ensure that
the user only enters valid input. Building a program with robust error
handling is much easier if it is decomposed into functions, so we will
introduce error handling and functions into our program together.

#### Step 3.1 - Starting word validation

Write a function called `get_start_word()` to get the starting word from the user.
First, create the function header:

	def get_start_word() -> str:


In Step 2.2, you wrote an `input` instruction to request the starting word. Copy it into
`get_start_word()`. On the next line, add a `return` statement to send the value
back to the function caller. Then replace the original input statement with a call
to `get_start_word()`, and make sure your program still runs and
behaves as before.

This sets up the structure for validating our input. By handling the input validation
in a function, we keep the `main()` code straightforward and uncluttered.

For English word validation, download the text file
<a href="../data/english3.txt" download>`english3.txt`</a>
and the Python module
<a href="../code/spellcheck.py" download>`spellcheck.py`</a>, and
make sure they are in the same project folder where you put your lab. At the top of your
Python program, you should write

    import spellcheck

which will allow you to use the functions in `spellcheck.py`.

The `spellcheck` module contains a function `valid_word(word,
filename)`, which returns `True` if the word is found in the file and
`False` otherwise.  You can call the function by writing something
like

    spellcheck.valid_word(some_word, 'english3.txt')

Handling erroneous input requires using a loop. The following example shows
a loop structure that you may find useful in completing
`get_start_word()`.  This is **just an example**; instead of checking
whether the word has four letters, you should check whether it is a
valid English word.

	valid = False
	while not valid:
		word = input("Enter a word that is at least four letters long: ")
		if len(word) < 4:
			print(f"{word} is less than four letters long. Please try again.")
		else:
			valid = True

Test your program in the Python Console before incorporating it into the rest of the program.
When you test it in the console, give it a few invalid words followed by a valid word to ensure
it behaves correctly.

Here is an example of how the program would behave with the error checking in place:

    What is the starting word? lig
	lig is not a word. Please try again.
	What is the starting word? log
    What is the ending word?

#### Step 3.2 - Ending word validation

Write a function to validate the ending word. This will be a slightly
more complex variation of the function you wrote in Step 3.1, as it
must ensure not only that the word is valid, but also that the word is
of the same length as the starting word. Here is the function
definition header:

	def get_end_word(start_word_length: int) -> str:

Replace your original `input` statement with a call to `get_end_word()` to ensure
that the ending word is valid and of the correct length. Test the function in the
Python Console first. Make sure it only allows words of the specified word length.
For example, if you test it as `get_end_word(5)`, it should only allow you to enter
words of length 5.

Here is a continuation of our earlier example to show how the program as a whole
should behave once you have incorporated `get_end_word()`:

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

#### Step 3.3 - Character index validation
Write a function to validate the user's input of a character index to change.
It should return an integer between 1 and the length of the current word. Any
non-integer or any integer outside that range should result in a message to
the user requesting suitable input. Here is the function declaration header:

	def get_index(current_word_len: int) -> int:

Replace your original `input` statement with a call to `get_index()` to ensure valid
input. Try `get_index(5)` in the Python Console. It should only allow you to enter numbers
from 1 to 5.

Here is a continuation of our earlier example to show how the program should behave:

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

#### Step 3.4 - Character validation
Write a function to ensure that the user inputs a single character. Here is
the function declaration header:

	def get_one_character() -> str:

Replace your original `input` statement with a call to `get_one_character()`.
Test it in the Python Console. Make sure it only allows single-character answers.
Try testing it by typing the Enter key without any input: it should ask the user
to try again in that case as well.

Here is a continuation of our earlier example to show how the program should
behave once you are using your function:

    Which character do you want to change? (the first character is 1) 1
    What is your new character? bb
	bb is more than one character. Please try again.
    What is your new character? b
	Current = BOG
    End     = BUG
    Which character do you want to change? (the first character is 1)

#### Step 3.5 - Word validation
Unlike the other error-handling steps, this step is straightforward to
implement without writing an additional function. Before committing
to the new word with the new character, make sure the new word obtained from calling
`swap_character()` is a valid word, again using the `spellcheck` module. If it is a
valid word, update your current word, the number of steps, and the solution path.
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

### Step 4 - Play

Once your program is working, use it to help you create at least two
puzzles, with solutions. One puzzle should be between two four-letter
words, requiring at least four steps; another puzzle should be between
two five-letter words, requring at least five steps.  If you would
like a challenge, you can try solving some of the puzzles below, and
include your solutions:

* FIRE -- HEAT
* SLEEP -- DREAM
* APE -- MAN

However, you are also welcome to create your own puzzles.  For
example, you could pick a starting word, and then use your program to
take valid steps until you reach another word you find interesting,
and use that as your puzzle.
