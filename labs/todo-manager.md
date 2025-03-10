---
layout: work
type: Lab
num: 6
worktitle: ToDo Manager
---

## Overview

In this lab, you will practice using lists and strings in Python by
implementing a very simple todo manager, which helps you keep track of
a list of things to do (or a list of anything at all).

Here's an example of what your program might look like by the end of
the lab:

    Welcome to the todo list manager!
    Enter the name of the file with your todos: todo.txt
    Warning, file todo.txt does not exist.
    ------------------------------
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 0
    Enter the new todo: Finish writing todo manager lab
    ------------------------------
    0) Finish writing todo manager lab
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 0
    Enter the new todo: Revise paper
    ------------------------------
    0) Finish writing todo manager lab
    1) Revise paper
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 0
    Enter the new todo: Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Finish writing todo manager lab
    1) Revise paper
    2) Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 2
    0) Finish writing todo manager lab
    1) Revise paper
    2) Beat all MK8 Deluxe tracks on 200cc mode
    Which todo do you want to replace? 1
    Enter the new todo: Revise paper for JFP
    ------------------------------
    0) Finish writing todo manager lab
    1) Revise paper for JFP
    2) Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 3
    Enter the search string: z
    No todos found matching 'z'.
    ------------------------------
    0) Finish writing todo manager lab
    1) Revise paper for JFP
    2) Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 3
    Enter the search string: t
    Todos matching 't':
    0) Finish writing todo manager lab
    1) Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Finish writing todo manager lab
    1) Revise paper for JFP
    2) Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 1
    0) Finish writing todo manager lab
    1) Revise paper
    2) Beat all MK8 Deluxe tracks on 200cc mode
    Which todo do you want to remove? 0
    ------------------------------
    0) Revise paper for JFP
    1) Beat all MK8 Deluxe tracks on 200cc mode
    ------------------------------
    0) Add a new todo
    1) Remove a todo
    2) Replace a todo
    3) Search
    4) Quit
    Your choice? 4

## Step 1: Bits and Pieces

Create a new Python file called `todo_manager.py`, and put
your name and date at the top.

Now follow the instructions below to write some functions you will
need.

#### 1.1 Turn a list into a string

Write a function called `list_into_lines(items: list[str]) -> str`.

Given a list of strings, this function should create a single string
that combines all of the strings from the list, putting a newline
character (`\n`) between each string. For example:

	>>> list_into_lines(['red', 'yellow', 'blue'])
	'red\nyellow\nblue'

You can also test your function like this:

	>>> print(list_into_lines(['red', 'yellow', 'blue']))
	red
	yellow
	blue

**Hint**: you should not need a `while` loop!  It is possible to
implement this function in only one line of code.  Look at your notes
from class!

**Hint**: make sure this function `return`s the result; it should not
`print` anything!

#### 1.2 Print Numbered List

Write a function called `print_numbered_list(items: list[str])`.

This function should take a list of strings as input and `print` them
out, one per line, with numbers in front of them.  For example, if
given the list `['hat', 'socks', 'shoes']` as input, it
should print out

    0) hat
    1) socks
    2) shoes

Unlike `list_into_lines`, this function's job is to actually `print`
something on the screen, not to `return` anything.

**Be sure to test your function** by right-clicking and choosing "Run File in Console"
and then trying your function with different inputs.  For example,
if you type

    print_numbered_list(['hat', 'socks', 'shoes'])

at the prompt, you should see the output shown above.


#### 1.3 Get choice

Write a function called `get_choice(prompt: str, choices: list[str]) -> int`.

This function takes as input a prompt string and a list of
choices, and returns an `int` corresponding to the
user's choice.  It should carry out the following steps:

  1. Print out a numbered list of the choices (using
    `print_numbered_list`).
  2. Prompt the user for `input` (using the provided `prompt`).
  3. Check to make sure the user's input is a number, and if so,
     that it corresponds to one of the choices.
  4. If the user's input is invalid, print an appropriate error
     message and simply **return** `-1`.  **Don't use a while loop
     to re-prompt the user.**  This will allow the user to "cancel"
     by entering an invalid input.
  5. Otherwise, if the user entered a valid choice, return the
     number they chose (be sure to return an `int`, not a string!).

**Again, you should be sure to load your file into the console and
test it**.  For example, you might see something like this:

    >>> get_choice("Whaddaya want? ", ['hat', 'socks', 'shoes'])
    0) hat
    1) socks
    2) shoes
    Whaddaya want? shirt
    Sorry, shirt is not a number.
    -1

    >>> get_choice("What color elephant? ", ['grey', 'blue', 'red'])
    0) grey
    1) blue
    2) red
    What color elephant? 5
    Sorry, 5 is not a valid choice.
    -1

    >>> get_choice("OK? ", ['sure', 'no way'])
    0) sure
    1) no way
    OK? 1
    1


## Step 2: Loading and Saving

A todo list manager isn't much good without being able to load and
save lists of todos!  You wouldn't want to have to type in all your
todos every time you run the program.

We have provided functions you can use to open and save text files.
Later in the semester we will learn more about how they work.  For
now, you can just copy and paste these functions into your program.

    # Open the file with the given name and return its contents as a list
    # of strings, one per line; OR print a warning and return the empty
    # list if there is an error opening the file (e.g. if the file does
    # not exist).
    def load_list_from_file(filename: str) -> list[str]:
        try:
            f = open(filename, 'r')
            lines = [l.rstrip() for l in f.readlines()]
            f.close()
            return lines
        except FileNotFoundError:
            print(f"Warning, file {filename} does not exist.")
            return []

    # Write the given string to the file with the given name.
    def save_file(filename: str, contents: str):
        try:
            f = open(filename, 'w')
            f.write(contents)
            f.close()
        except:
            print(f"Something went wrong saving {filename}!")

Now define a function `main()` which does the following:

  1. Prompt the user for the name of the file containing their todo list.
  2. Open the file (using the `load_list_from_file` function) and store
     the returned list in a variable.
  3. Add a fake todo item to the end of the list (this part is just
     temporary, to make sure everything else is working; you will
     remove it in the next step).
  4. Print out the todo list using `print_numbered_list`.
  5. Save the new, extended list back to the file using the `save_file`
     function (see the next paragraph for a helpful hint).

Note that `save_file` expects a string, not a list of strings,
so you will have to call `list_into_lines` to turn your list of strings
into a single string before calling it.

Again, you should be sure to test your `main()` function. (You can use
whatever file name you want for your todo list; if it doesn't already
exist, it will be created by `save_file`.)  You should be able to tell
if the loading and saving is working since every time you run `main()`
your todo list should have one additional item added to the end.

## Step 3: Menu

Now we will modify your `main()` function so it lets the user
repeatedly choose options from a menu.

First, create a list of strings representing the different menu
choices that will be available to the user: there should be an option
to add a todo, remove a todo, replace a todo, search for a todo, or
quit.

Now, delete the code from `main()` thats adds a fake todo item to the
end and prints the list (steps 3 and 4 above), and replace it with a
loop:
* The loop will exit when the user selects option `4`.
* At each iteration of the loop:
  * Using `print_numbered_list`, display the current todo list.
  * Using `get_choice`, request a menu option from the user, using the
    list of menu options you created earlier.

At this point the only active menu choice is the option to
quit. Nothing will actually happen when you choose anything else from
the menu; you will fix that in the next step.

## Step 4: Operations

Now it's time to actually implement the operations!  Below are
descriptions of what the different menu choices should do.  You can
also look at the example program output at the top of this lab for
inspiration.

**Be sure to test that each operation works before moving on to the
next!**

#### 4.1 add

If the user chooses to add a new todo item, you should prompt them for
a new todo and add it to the end of the list.

#### 4.2 remove

If the user chooses to remove a todo item, you should
use `get_choice` to ask for the index of the item they
would like to remove.  If `get_choice`
returns `-1`, do nothing.  Otherwise, you can use
the `pop` list function to remove the item at a particular
index, for example, if your list of todos is called `todos`
and the user's choice is stored in a variable
called `choice`, you could
write `todos.pop(choice)`.

#### 4.3 replace

This should work similarly to remove: ask the user which item they
would like to replace; if they make a valid choice, prompt them for a
new todo item, and replace the item at the index they chose.  (*Hint*:
replacing an item should be only one line of code!  Look in your notes
from class if you don't remember how to do it.)

#### 4.4 find_all()

Write a function
<pre>
def find_all(term: str, items: list[str]) -> list[str]:
</pre>
which takes a search term and a list of items, and returns the list of
only those items from the list which contain the search term.  You can
check whether one string contains another string using
the `in` operator: for example, `"th" in
  "python"` will return `True`, but `"z" in
  "python"` is `False`.

Test your function in the console: for example, you should get
<pre>
>>> find_all("ab", ["baby", "dog", "cat", "absolute", "table", "python"])
["baby", "absolute", "table"]
</pre>

#### 4.5 search

Now implement the search menu choice: prompt the user what they want
to search for, use `find_all` to get the todos that match
their search term, and display them to the user
using `print_numbered_list`.

At this point you should be able to reproduce something similar to
the example program run shown at the beginning of the lab!  Note,
however, that your output does not need to be identical to the
example shown.  Feel free to use your creativity to make it look
nice or add your own extra features.
