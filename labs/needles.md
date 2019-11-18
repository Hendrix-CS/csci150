---
layout: work
type: Lab
num: 12
worktitle: Needles and Haystacks
---

Overview
--------

Enron was an energy trading company. In October 2001, the [Enron
Scandal](https://en.wikipedia.org/wiki/Enron_scandal) became public
knowledge. Among other aspects, there were two crucial ingredients of
the scandal:

1.  Incriminating documentation was systematically destroyed.
2.  Fraudulent practices were employed to artificially drive up energy
    prices.

Some key evidence employed by prosecutors was obtained through the
seizure of the archived email messages on the company's servers. These
emails were [released publicly](https://www.cs.cmu.edu/~./enron/) in the
aftermath of the scandal. This email archive is frequently employed by
computer scientists for experimenting with ideas for large-scale text
processing. In this lab, we will write Python code to enable us to
explore this archive. In the process, you might be able to identify some
of the key incriminating emails that it contains.

File System Structure
---------------------

The files on a computer are organized in a hierarchy. You are likely
accustomed to navigating this hierarchy using the metaphor of the
**folder**. Each folder contains files, some of which might be other
folders. By placing folders within folders, we can create a hierarchical
layout of all of our data. Because a folder can be placed within another
folder, we call this a **recursive data structure**. To navigate a
recursive data structure, the most effective technique is to write
**recursive functions**, that is, functions that call themselves.

Step 1: Exploring File System Functions
---------------------------------------

Create a new Python project for lab 8. [Download the Enron email
repository](http://ozark.hendrix.edu/~ferrer/courses/150/s19/labs/lab8/lab8.zip),
unzip the compressed archive, and place it in your project directory.
(**Note:** This is **not** the full repository. We have edited it down
to make it easier for you to analyze.) Then download the Python file
named **[`filefuncs.py`]({{site.baseurl}}/code/filefuncs.py)** and also place it in your project directory. At
the top of the file is the line `import os`. This imports important
functions for accessing the computer's operating system. We are
specifically interested in the following functions:

-   `os.listdir()`: This function returns a list of all files in a
    specified folder.
-   `os.path.isdir()`: This function returns true if a given file is
    another folder, and false otherwise.

Using `os.listdir()`, we can examine each file in a given folder. If it
is a regular file, we can process it however we like. If it is another
folder, we can use recursion to process the files within it. The
following short function is included in the file and demonstrates how
these two functions are to be used:

    def files_and_folders(path: str):
        i: int = 0
        files: List[str] = os.listdir(path)
        while i < len(files):
            child: str = path + os.sep + files[i]
            if os.path.isdir(child):
                print(child + " is a folder")
            else:
                print(child + " is a regular file")
            i += 1

Run your file in the console, and then type the following lines in the
console to see what it does:

    files_and_folders('.')
    files_and_folders('lab8')
    files_and_folders('lab8/townsend-j')
    files_and_folders("lab8/townsend-j/to_do")

What is the output of each command? What is the meaning of this output?
Write down your answers in a comment above the definition of the
`files_and_folders()` function. Next, add these two lines to the `else`
clause:

                contents = open(child).read()
                print(contents)

Run your file in the console, then run `files_and_folders('.')` again,
as well as `files_and_folders("lab8/townsend-j/to_do")`. What does it do
differently? What is the effect of `open(child).read()`? Add your
answers to the comments above the function.

Step 2: Finding the depth
-------------------------

The Enron emails are organized using a system of folders. Each folder
corresponds to a specific person. Each person might have other folders
to better organize their emails. In this step, we will write a function
to find out how deep a particular folder goes. This function is outlined
as follows:

    def find_depth(path: str) -> int:
        # set an integer variable representing the deepest path to zero
        # for each file in the current folder
            # If it is a folder
              # Call find_depth recursively on that folder, storing the result in a variable.
              # If the returned value, plus 1, is greater than our deepest path so far,
              #   set our deepest path to be that value. Otherwise, do nothing.
        # return the deepest path

Here's an example of using this function. (You should get the same
answer when you test it.)

    >>>find_depth('lab8')
    6

Step 3: Counting all the files
------------------------------

In this step, we will count the total number of files that are stored in
the folder. The outline of this function will be very similar to the
outline of the previous function. The difference is that instead of
finding the maximum depth, we want to know the total number of files.
So, inside our loop, if a given file is a folder, we add to our total
the result of the recursive call. If not, we add 1 (to count that as a
normal file).

    def file_count(path: str) -> int:
        # set an integer variable representing the total number of files to zero
        # for each file in the current folder
            # If it is a folder
              # Call file_count recursively on that folder, adding the result to our total
            # Otherwise
              # Add 1 to our total
        # return the total

Here's an example of using this function. (You should get the same
answer when you test it.)

    >>>file_count('lab8')
    57114

Step 4: Finding target strings
------------------------------

To detect clues of wrongdoing, we can write a function to visit every
file and see if it contains certain target words. In this step, our
function will return a list containing the name of every file that
contains a target word. We can then use this list to decide which files
to manually inspect.

    def all_files_with(path: str, target_string: str) -> List[str]:
        # set a variable representing all the filenames containing target_string to the empty list
        # for each file in the current folder
            # If it is a folder
              # Call all_files_with on that folder, adding every element from the list it returns
              #  to our own list.
            # Otherwise
              # Open the file and read it into a string.
              # If the string contains our target_string, add the filename to our list.
        # return our list of filenames

Step 5: Finding evidence
------------------------

At this point, we have available the tools to try to find a needle in
the haystack. Here are some text strings you might consider using to
find culpable emails:

-   jail
-   irregularities
-   fear of litigation
-   witholding capacity
-   interruptible transmission
-   found liable
-   market interference
-   special purpose entity
-   possession of tapes

Step 6: Assessing evidence
--------------------------

Identify a collection of filenames of emails that you think might
contain evidence of wrongdoing. What aspects of those emails might
provide evidence? Are there any ambiguities? In what ways is the
evidence incomplete or inconclusive? Provide answers in your Evaluation
Document.
