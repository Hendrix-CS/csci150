---
layout: work
type: Homework
num: 9
worktitle: File I/O
---
*Due: Monday, October 28*

Write two functions:
1. The first function, `list_output()`, should write each element of a list to a separate line of a file.
Each item should be prefixed by its index.  For example:

```
items = ['alpha', 'beta', 'gamma']
list_output("letters.txt", items)
```

should create the following file:
```
0 alpha
1 beta
2 gamma
```

Note -- `list_output()` takes **two** parameters -- a string, which is the name of the output file, and the list.
`list_output()` should not `return` anything! It simply creates a file.

2. The second function, `list_input()`, should read in a file in the above format and reconstruct the
original list. So, `list_input()` should take in a single string as a parameter, the name of the input file. `list_input()` should return a single list.

NOTE: Please consider the following:
- It is possible that the list for `list_input()` has more than 10 entries, so that you cannot assume the "data" of the list starts in position 2 when reading in the data file
- It is also possible that entries in the list themselves have spaces -- you'll need to `find` the first occurrance of a space in each line when parsing the file in `list_input()`
