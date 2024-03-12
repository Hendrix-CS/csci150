---
layout: work
type: Homework
num: 9
worktitle: File I/O
---

Write two functions:
1. The first function, `list_output()`, should write each element of a list to a separate line of a file.
Each item should be prefixed by its index.  For example:

```
items = ['a', 'b', 'c']
list_output("letters.txt", items)
```

should create the following file:
```
0 a
1 b
2 c
```

2. The second function, `list_input()`, should read in a file in the above format and reconstruct the
original list.