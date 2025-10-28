---
layout: work
type: Homework
num: 9
worktitle: Dictionaries
---

Suppose that the following dictionary is created, which indicates the (made up) number of currently declared
majors in some Natural Sciences departments:

`d = {'CHEM': 19, 'CSCI': 37, 'MATH': 23, 'PHYS': 13}`

1. What are the following values:

  - `d['MATH']`
  - `d['CSCI']`
  - `d['CHEM'] / 2'

2. You learn that three new students have declared Computer Science as their major. How could you updated the dictionary?
Write actual code to do this!

3. If there are 15 Biology majors, how would you update the dictionary?

4. Using the original version of `d = {'CHEM': 19, 'CSCI': 37, 'MATH': 23, 'PHYS': 13}` above, what would be 
the value of `c` after the following code runs?

```python
c = 0
for k in d:
  if 'h' in k:
    c += d[k]
```


Write two functions:
5. The first function, `vowel_histogram(s: str) -> Dict[str,int]`, should return a dictionary
where the keys are vowels (a, e, i, o, u) and the values are the number of occurrences of each
vowel in the string. Here is an example of calling the function in the console:

```
>>> vowel_histogram('This restaurant is a long way from our house.')
{'a': 4, 'e': 2, 'i': 2, 'o': 4, 'u': 3}
```

6. The second function, `min_key(d: Dict[str, int]) -> str`, should return the key in the 
dictionary with the smallest value. Here is an example of calling the function in the console:

```
>>> min_key({'a': 4, 'b': -5, 'c': 2, 'd': -7, 'e': 4})
'd'
```
If the smallest key happens to occur more than once, a solution which returns any key (associated with that value) will be considered correct.
